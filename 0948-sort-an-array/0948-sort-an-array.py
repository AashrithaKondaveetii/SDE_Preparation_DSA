class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Swapping Logic
        # def swap(i, j):
        #     temp = nums[i]
        #     nums[i] = nums[j]
        #     nums[j] = temp

        # ---Selection Sort
        # for i in range(0, len(nums) - 1):
        #     min_idx = i
        #     for j in range(i+1, len(nums)):
        #         if (nums[j] < nums[min_idx]):
        #             min_idx = j
        #     if (min_idx != i):
        #         swap(i, min_idx)
        # return nums

        # ---Bubble Sort---
        # for gap in range(1, len(nums)):
        #     swapped = False
        #     for i in range(0, len(nums) - gap):
        #         if (nums[i] > nums[i + 1]):
        #             swap(i, i+1)
        #             swapped = True
        #     if (not swapped):
        #         break
        # return nums

        def merge(arr, L, M, R):
            left, right = arr[L : M+1], arr[M+1 : R+1]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
            return

        def mergeSort(arr, l, r):
            if l == r:
                return
            m = l + (r - l) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return

        mergeSort(nums, 0, len(nums) - 1)
        return nums

