class Solution:
    # Time: O(n) since work is never redone if any of the later integers were already part of the sequence
    # Space: O(n) since we store a set of the list, and a dictionary with each element of the set
    # NOTE: Make sure you set up whether you want your recursion to return something or just modify a data structure

    def longestConsecutive(self, nums: List[int]) -> int:
        seq_dict = dict()
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            self.recSeq(num, num_set, seq_dict)
            max_len = max(max_len, seq_dict[num])

        return max_len

    def recSeq(self, num, num_set, seq_dict):
        if num in seq_dict:
            return
        
        if num-1 not in num_set:
            seq_dict[num] = 1
            return
        
        self.recSeq(num-1, num_set, seq_dict)
        seq_dict[num] = seq_dict[num-1] + 1
        