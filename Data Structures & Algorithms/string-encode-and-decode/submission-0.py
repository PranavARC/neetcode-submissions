class Solution:
    '''
    We mark the start of each string with "S"
    Every character of the string is switched to its Unicode integer
    Each character is separated by a comma
    Each string is separated by a space
    '''
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str += "S,"
            for char in st:
                encoded_str += str(ord(char)) + ","
            encoded_str += " "
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        word_list = s.split()

        for word in word_list:
            char_list = word.split(",")
            curr_str = ""
            for char in char_list:
                if char in ("", "S"):
                    continue
                curr_str += chr(int(char))
            decoded_list.append(curr_str)
        
        return decoded_list