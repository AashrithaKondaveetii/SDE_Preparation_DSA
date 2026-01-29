class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSum = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in hashSum:
                return [i, hashSum[diff]]
            hashSum[j] = i