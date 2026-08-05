class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue if current number is too large
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # Move to the next index (cannot reuse the same element)
                backtrack(i + 1, path, remaining - candidates[i])

                path.pop()

        backtrack(0, [], target)
        return ans