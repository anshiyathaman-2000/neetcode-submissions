class Solution:
    def permute(self, nums):
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            # Base case
            if len(path) == len(nums):
                result.append(path[:])
                return

            # Try every unused number
            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return result