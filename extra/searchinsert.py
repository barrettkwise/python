import bisect
def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return bisect.bisect_left(nums,target,lo=0,hi=len(nums))
