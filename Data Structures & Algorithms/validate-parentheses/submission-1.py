class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {']': '[', ')': '(', '}': '{'}
        open_bracks = set(tuple(bracket_dict.values()))
        open_list = []
        for char in s:
            if char in open_bracks:
                open_list.append(char)
            elif char not in bracket_dict:
                return False
            elif len(open_list) == 0 or open_list.pop() != bracket_dict[char]:
                return False
            
        return len(open_list) == 0
