class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            for j in range(1,n):
                if i!=j:
                    sum1=numbers[i]+numbers[j]
                    if sum1==target:
                        return [i+1,j+1]