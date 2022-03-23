from types import NoneType


people = [
         {"name" : "john", "attributes" : ("cool", "strong", "tall")},
         {"name" : "connor", "attributes" : ("fast", "smart", "tall")},
         {"name" : "bill", "attributes" : ("cool", "fast", "tall")}
         ]

q1 = "is your character cool?"
q2 = "is your character strong?"
q3 = "is your character fast?"
q4 = "is your character smart?"
q5 = "is your character tall?"
questions = [q1, q2, q3, q4, q5]

def questionask():
    charattributes = []
    i = 0
    while i < len(questions):
        print(questions[i])
        answer = str(input("true or false?"))
        answer.lower()
        if answer == "yes" or answer == "y" or answer == "true":
            charattributes.append(questions[i][18:-1])
            i = i + 1
        else:
            i = i + 1

    selectchar(charattributes)
    add = str(input("add character?"))
    add.lower()
    if add == "y" or add == "yes":
        addcharacter()

def selectchar(charattributes: list) -> None:
    index = 0
    while index < 3:
        temp1 = " ".join(charattributes)
        temp2 = " ".join(people[index]["attributes"])
        if temp1 == temp2:
            person = ""
            person = "".join(people[index]["name"])
            print(f"your person is {person}.")
            break

        index = index + 1

    if index == 3:
        print("no person found")

def addcharacter():
    name = str(input("name?"))
    attribute = str(input("attributes? (format as 1,2,3)"))
    attribute = attribute.split(",")
    attribute = (attribute[0], attribute[1], attribute[2])
    people.append({"name":name, "attributes":attribute})
    print(people)

def main():
    flag = True 
    while flag == True:
        questionask()
        choice = str(input("continue?"))
        choice = choice.lower()
        if choice == "n" or choice == "no":
            flag = False

main()
