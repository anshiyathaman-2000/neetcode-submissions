class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_count = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1

            max_count = max(max_count, count[ch])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans