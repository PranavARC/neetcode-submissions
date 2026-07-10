class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n), since the pointers move through the list linearly, never repeating elements
        # Space: O(n), since we might store the entire string in the set
        if len(s) < 2:
            return len(s)
        max_len = 1
        left = 0
        right = 1

        letter_set = set((s[left],))

        while right < len(s):
            if left >= right:
                letter_set.add(s[right])
                right += 1
            elif s[right] in letter_set:
                letter_set.discard(s[left])
                left += 1
            else:
                max_len = max(max_len, right - left + 1)
                letter_set.add(s[right])
                right += 1
        
        return max_len
