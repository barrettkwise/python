def sortArrayByParity(nums):
    if len(nums) == 1: return nums
    return sorted(nums,key = lambda x: x % 2)
