class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        arr=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s==0:
                    arr.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif s<0:
                    left+=1
                else:
                    right-=1
        return arr
