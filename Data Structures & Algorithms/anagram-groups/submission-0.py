class Solution:
    # Create a frequency dict of each string, check if it exists in a dictionary, put the string into the frequency dict's sublist
    # Time = O(n x m), Space = O(m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for str1 in strs:
            str1_dict = dict()
            for char in str1:
                if char not in str1_dict:
                    str1_dict[char] = 0
                str1_dict[char] += 1
            str1_items = frozenset(str1_dict.items())

            if str1_items not in anagram_dict:
                anagram_dict[str1_items] = []
            anagram_dict[str1_items].append(str1)
        
        return list(anagram_dict.values())

    """
    # Sort each string, check if the sorted string exists in a dictionary, put the unsorted string into the sorted string's sublist
    # Time = O(nlogn x m), Space = O(mxn) [since the string used in the keys can be up to n letters each]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for str1 in strs:
            str2 = str(sorted(str1))
            if str2 not in anagram_dict:
                anagram_dict[str2] = []
            anagram_dict[str2].append(str1)
        return list(anagram_dict.values())
    """

    """
    # Check if the current string is an anagram of any of the sublists, if so add it to the sublist, else make a new one for it
    # Time = O(m^2 x n), Space = O(m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_lists = []
        for str1 in strs:
            sublisted = False
            for sublist in anagram_lists:
                if self.anagramCheck(str1, sublist[0]):
                    sublist.append(str1)
                    sublisted = True
                    break
            if not sublisted:
                anagram_lists.append([str1])
        
        return anagram_lists

    def anagramCheck(self, str1, str2):
        if len(str1) != len(str2):
            return False
        
        str1_dict = dict()

        for char in str1:
            if char not in str1_dict:
                str1_dict[char] = 0
            str1_dict[char] += 1
        
        for char in str2:
            if char not in str1_dict:
                return False
            str1_dict[char] -= 1
            if str1_dict[char] == 0:
                str1_dict.pop(char)
        
        return len(str1_dict) == 0
    """
