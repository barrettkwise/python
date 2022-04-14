def maxSubArray(nums) -> int:
    ##adds numbers one at a time
    ##and compares sum to current max sum
        
    curr_sum = 0
    max_sum = nums[0]
        
    for i in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += i
        max_sum = max(curr_sum, max_sum)
        print(f"current: {curr_sum}")
        print(f"max: {max_sum}")
        
    return max_sum
