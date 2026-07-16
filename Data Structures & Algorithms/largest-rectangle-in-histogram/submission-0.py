class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                nse = i
                pse = stack[-1] if stack else -1

                max_area = max(max_area, height * (nse - pse - 1))

            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            nse = n
            pse = stack[-1] if stack else -1

            max_area = max(max_area, height * (nse - pse - 1))

        return max_area