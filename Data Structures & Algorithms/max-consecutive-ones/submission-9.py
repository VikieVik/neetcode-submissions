class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for e in nums:
            if e == 1: 
                count+=1
                print("1 found", count)
            if e == 0: 
                print("0 found")
                res=max(count, res)
                print("res", res)
                count=0
        result = max(count, res)
        return result



        