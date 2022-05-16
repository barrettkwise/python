#!/usr/bin/env python
# coding: utf-8

# In[2]:


from qiskit import IBMQ

IBMQ.load_account()

get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.circuit.library.standard_gates import RYGate
from qiskit.circuit import Parameter


# In[3]:


provider = IBMQ.load_account()

from qiskit import QuantumCircuit, IBMQ, execute, Aer, QuantumRegister, ClassicalRegister 
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor,backend_overview 
from qiskit.visualization import plot_histogram
import math 


# In[87]:


def parabola(l):
    data_ = []
    for i in range(l):
        value = math.pow(l/2, 2) - math.pow(abs(i - l/2), 2)
        print(value)
        data_.append(value)
    return data_
    
def sine(l):
    data_ = []
    for i in range(l):
        value = 1 + math.sin((20*i / 180) * math.pi)
        print(value)
        data_.append(value)
    return data_

def pi(l):
    
    the_pi = "3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767"
    data_ = []
    for i in range(l):
        value = int(the_pi[i])
        data_.append(value)
    return data_
    

def normalizeData(data_points):
    divider = 0
    sum = 0
    print("Amplitudes: ")
    for point in data_points:
        divider += math.pow(point, 2)
    divider = math.sqrt(divider)
    normalized = []
    for i in range(len(data_points)):
        x = data_points[i] / divider
        x2 = math.pow(data_points[i] / divider, 2)
        print(round(x2, 3))
        sum += x2
        normalized.append(x)
    
    return (normalized, divider)

def gen_angles(data):
    if len(data) > 1:
        new_length = int(len(data) / 2)
        new_data = []
        for k in range(new_length):
            new_data.append(math.sqrt(math.pow(data[2*k], 2) + math.pow(data[2*k + 1], 2)))
        
        #print("value")
        #print(new_data)
    
        inner_angles:List[float] = gen_angles(new_data)
    
        angles = []
        
        for k in range(len(new_data)):
            if new_data[k] != 0:
                inside = data[2*k + 1] / new_data[k]
                print(round(inside, 4))
                if (data[2*k] > 0):
                    angles.append(2 * math.asin(inside))
                else:
                    angles.append(2 * math.pi - 2 * math.asin(inside))
            else:
                angles.append(0.0)

        angles = inner_angles + angles
        return angles
    else:
        return []
    
def getCtrlState(level, k):
    ctrl_decimal = int(abs(k - (math.pow(2, level) - 1)))
    ctrl_bin = str(bin(ctrl_decimal))
    ctrl_str = ctrl_bin.split('b')[1].zfill(level)
    ctrl_str = ''.join(reversed(ctrl_str)) ### Reverse because of Qiskit's most significant bit convention 
    return ctrl_str


### Main program 

pi_result = True 
data_length = 8
data_points = pi(data_length) # 2^n long data vector
    
pair = normalizeData(data_points)
data = pair[0]
key = pair[1]

print("Key")
print(key)
print("")
print("Angles: ")
angles = gen_angles(data)

nqubits = int(math.log2(len(data_points)))
nclassical = nqubits
q = QuantumRegister(nqubits)
c = ClassicalRegister(nclassical)
circ = QuantumCircuit(q, c)

a = Parameter('a')
CCRY = RYGate(a).control(2, ctrl_state = '10')

print("Levels:")

for k in range(len(angles)):  # now works
    j = 0
    if (k > 0):
        j = int(math.log2(k + 1)) # level in the binary tree 
    
    print(j)
    
    if (j == 0):
        circ.ry(angles[k], nqubits - 1 - j)
        
    
    """for i in range(j):
        if(index(i, j, k)):
            circ.cry(angles[k], nqubits - 1 - i, nqubits - 1 - j, ctrl_state = 1) # adding 0.27 to angle helped with accuracy 
        else:
            circ.cry(angles[k], nqubits - 1 - i, nqubits - 1 - j, ctrl_state = 0)
    """
    if (k == 1):
        circ.cry(angles[k], nqubits - 1, nqubits - 1 - j, ctrl_state = 0)
    elif(k == 2):
        circ.cry(angles[k], nqubits - 1, nqubits - 1 - j, ctrl_state = 1)
    elif(k > 2):
        ctrl = getCtrlState(j, k)
        CCRY = RYGate(angles[k]).control(j, ctrl_state = ctrl)
        qubits = []
        for i in range(j + 1):
            qubits.append(nqubits - 1 - i)
        circ.append(CCRY, qubits)
            
    """
    if (j == 0):
        circ.ry(angles[k], 0)
    else:
        if (j == 1):
            circ.ry(angles[k], 1)
            circ.cry(angles[k], 0, 1)
        else:
            circ.ry(angles[k], 2)
            circ.cry(angles[k], 0, 2)
            circ.cry(angles[k], 1, 2)"""
    
circ.barrier()
circ.measure(q, c)
circ.draw(output='mpl')


# In[88]:




provider = IBMQ.get_provider()
provider.backends() 
local_sim_backend = Aer.get_backend('qasm_simulator') 
sim_backend = provider.get_backend('ibmq_qasm_simulator') 
### real_backend = least_busy(provider.backends(simulator=False)) # old


real_backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= nqubits 
                                       and not x.configuration().simulator 
                                       and x.status().operational==True))

print("least busy backend: ", real_backend)

print(real_backend) 
job1 = execute(circ,local_sim_backend) 
job2 = execute(circ,sim_backend)
job3 = execute(circ,real_backend)
job_monitor(job3) 

counts1 = job1.result().get_counts()
counts2 = job2.result().get_counts()
counts3 = job3.result().get_counts()  # may be commented out to speed up testing


shots = job3.result().to_dict()["results"][0]["shots"]
measured_results = []

for i in range(len(counts3)):
    binary_state = str(bin(i))
    binary_state = binary_state.split('b')[1].zfill(nqubits)
    print(binary_state, end = ' | ')
    measured_result = math.sqrt(counts2[''.join(binary_state)] / shots) * key
    measured_results.append(measured_result)
    print("%3.3f" % measured_result, end = ' \n')

if (pi_result):
    
    str_result = ""
    for k in range(len(measured_results)):
        if (k == 0):
            str_result = str_result + str(round(measured_results[k]))
            str_result = str_result + "." 
        else:
            str_result = str_result + str(round(measured_results[k]))
        
    print(str_result)

legend = ['Local simulator', 'Remote simulator', 'Real processor']
 
circ.draw()

plot_histogram([counts1, counts2, counts3], legend=legend, bar_labels = True)


# In[ ]:


the_pi = "3.141592653589793238462643383279502884197169399"


# In[ ]:




