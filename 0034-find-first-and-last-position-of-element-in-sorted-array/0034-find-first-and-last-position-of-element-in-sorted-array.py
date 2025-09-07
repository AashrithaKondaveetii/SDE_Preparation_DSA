class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = self.findBound(nums, target, True)
        upper = self.findBound(nums, target, False)
        if lower == -1:
            return [-1, -1]
        return [lower, upper]
    

    def findBound(self, nums: List[int], target: int, isFirst: bool):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2

            if nums[mid] == target:
                if isFirst:
                    if mid == l or nums[mid - 1] < target:
                        return mid 
                    else:
                        r = mid - 1
                else:
                    if mid == r or nums[mid + 1] > target:
                        return mid
                    else:
                        l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return - 1