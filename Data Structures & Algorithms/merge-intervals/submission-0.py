from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Step 1: Sort intervals by starting value
        intervals.sort()

        # Step 2: Store first interval
        result = [intervals[0]]

        # Step 3: Check remaining intervals
        for start, end in intervals[1:]:

            # Last interval in result
            last_end = result[-1][1]

            # If overlapping
            if start <= last_end:
                result[-1][1] = max(last_end, end)

            # If not overlapping
            else:
                result.append([start, end])

        return result