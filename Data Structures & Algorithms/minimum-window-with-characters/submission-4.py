class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Create a set of all of the non-dupe t letters, and create a freq dict stating how many of them are required
        go down the string with a left pointer starting at 0
        When we land upon a character that exists in t, we check if the freq dict for that letter is at 0
        If it's not, we reduce it by 1 and continue
        If so, we move our left pointer to the next index that has a t element
        (If this is the first t character, we just move left to there regardless)
        (Once every t element is covered, we set a certain boolean to true and record the current L - R indices)
        (if we ever move left again, check if this new L/R is a shorter substring)
        (by the end, return the string between L and R, or return nothing if substring doesn't exist)
        '''
        letter_set = set()
        freq_dict = dict()
        for char in t:
            letter_set.add(char)
            freq_dict[char] = 1 + freq_dict.get(char, 0)
        
        best_left = -1
        best_right = -1
        t_indices = []
        curr_t = 1

        left = 0
        for right in range(len(s)):
            char = s[right]
            if char not in freq_dict:
                continue
            
            if char in freq_dict:
                freq_dict[char] -= 1
                if freq_dict[char] == 0:
                    letter_set.discard(char)


                if best_left == -1:
                    best_left = right
                    left = right
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