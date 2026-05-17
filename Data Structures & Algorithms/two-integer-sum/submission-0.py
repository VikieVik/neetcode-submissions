class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} #val: index
        for i, n in enumerate(nums):
            complement = target - n 

            if complement in nums_map: 
                return [nums_map[complement], i]
            nums_map[n] = i
