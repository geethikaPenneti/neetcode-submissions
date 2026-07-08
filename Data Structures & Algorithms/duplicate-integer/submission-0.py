class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        nums.sort()
        ct=0
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                ct+=1
                if ct>=1:
                    return True
        return False      