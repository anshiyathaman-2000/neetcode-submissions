from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            # If we reach the target, save the combination
            if total == target:
                result.append(path[:])
                return

            # If total exceeds target, stop exploring
            if total > target:
                return

            # Try every number starting from 'start'
            for i in range(start, len(nums)):
                path.append(nums[i])              # Choose
                backtrack(i, path, total + nums[i])  # Reuse same number
                path.pop()                       # Undo choice

        backtrack(0, [], 0)
        return result