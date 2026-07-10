class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n), since the pointers move through the list linearly, never repeating elements
        # Space: O(n), since we might store the entire string in the set
        # NOTE: Redid this in order to better implement sliding window (aka always moving right
        # and having a condition such that left can never move past right, since an empty window fulfills the condition) 
        max_len = left = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
