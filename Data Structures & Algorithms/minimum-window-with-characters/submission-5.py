class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Create a set of all of the non-dupe t letters, and create a freq dict stating how many of them are required
        go down the string with a left pointer starting at 0
        When we land upon a character that exists in t, we decrement its count in the freq dict
        If its frequency is 0, we remove it from the letter set (used to check if we've covered all the required chars)
        If this is the first t character we found, we automatically set left to this (since nothing before matters)
        Else if the required frequency of our current character is negative (aka we already have more than enough of this in the substr),
        We perform a loop to move up the left pointer on the following basis:
        If the left char isn't required, we incremement left
        If the left char is required, but its frequency is negative, we increment the letter's frequency but increment left
        But if it's required, and the frequency is 0 or more (aka we either have just enough or not enough iterations of the char), we stop
        And if the letter set is ever empty after any we encounter a t-char (meaning we covered every t-letter),
        Check if the current L-R yields a shorter substring than the previously best L-R or if that previous best doesnt exists
        If so, set these as the new best L-Rs
        By the end, return the string between L and R, or return nothing if substring doesn't exist
        Time: O(n) [Creation of dict/set, letter check and frequency decrement, L always moves linearly forward, and set length check is also linear]
        Space: O(n) [The dictionary/set can only be as long as the string]
        '''
        letter_set = set()
        freq_dict = dict()
        for char in t:
            letter_set.add(char)
            freq_dict[char] = 1 + freq_dict.get(char, 0)
        
        best_left = best_right = -1

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char not in freq_dict:
                continue
            
            freq_dict[char] -= 1
            if freq_dict[char] == 0:
                letter_set.discard(char)

            if best_left == -1:
                best_left = left = right
            elif freq_dict[char] <= 0:
                while True:
                    if s[left] in freq_dict:
                        if freq_dict[s[left]] >= 0:
                            break
                        else:
                            freq_dict[s[left]] += 1
                    left += 1
        
            if len(letter_set) == 0:
                if best_right == -1 or best_right - best_left > right - left:
                    best_left = left
                    best_right = right

        if best_right != -1:
            return s[best_left:best_right+1]
        else:
            return ""