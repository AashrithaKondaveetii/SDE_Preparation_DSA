class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxW, totalW = -1, 0
        for weight in weights:
            maxW = max(maxW, weight)
            totalW += weight
        left, right = maxW, totalW
        while left < right:
            mid = left + (right-left) // 2
            daysNeeded, currW = 1, 0
            for weight in weights:
                if currW + weight > mid:
                    daysNeeded += 1
                    currW = 0
                currW += weight
            if daysNeeded > days:
                left = mid + 1
            else:
                right = mid 
        return left

        