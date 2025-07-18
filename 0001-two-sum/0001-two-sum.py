class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i, j in enumerate(nums):
            difference = target - j
            if difference in prev_map:
                return [prev_map[difference], i]
            prev_map[j] = i
        