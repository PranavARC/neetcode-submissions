class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n), since sanitizing the string is O(n) and iterating through the cleaned string is O(n)
        # Space: O(n), since we create a santized string, could be O(1) if we were willing to perform sanitization on the fly
        # aka skipping non-alnum characters, and setting each char to lowercase where applicable

        clean_str = ""
        for char in s:
            if not char.isalnum():
                continue
            
            if char.isalpha():
                char = char.lower()
            
            clean_str += str(char)
        
        for i in range(0, len(clean_str)//2):
            if clean_str[i] != clean_str[-(i+1)]:
                return False
        
        return True
