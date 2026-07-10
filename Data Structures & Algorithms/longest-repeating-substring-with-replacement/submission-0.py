class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time: O(n) since we move through the array linearly, and the max operation will always be O(26) [26 letters] aka O(1)
        # Space: O(n) since we store each unique character in the dictionary (though only 26 characters means you could argue O(26) = O(1))
        
        char_dict = dict()
        left = max_len = 0

        for right in range(len(s)):
            char_dict[s[right]] = 1 + char_dict.get(s[right], 0)
        
            while right - left + 1 - max(char_dict.values()) > k:
                char_dict[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len
