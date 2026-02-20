class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxA = max(maxA, height * (i - idx))
                start = idx
            stack.append((start, h)) 
        
        for i, h in stack:
            maxA = max(maxA, h * (len(heights) - i)) #len(heights) because its the starting point
        return maxA