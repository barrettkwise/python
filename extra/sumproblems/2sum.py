class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevTable = {}
        
        for i,currVal in enumerate(nums):
            complement = target - currVal
            if complement in prevTable:
                return [prevTable[complement],i]
            prevTable[currVal] = i
