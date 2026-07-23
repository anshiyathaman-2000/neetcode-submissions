from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxFreq = max(freq.values())

        countMax = 0
        for count in freq.values():
            if count == maxFreq:
                countMax += 1

        intervals = (maxFreq - 1) * (n + 1) + countMax

        return max(len(tasks), intervals)