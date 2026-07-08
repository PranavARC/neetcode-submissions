class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(nlogn) (for sorting the dict items), Space: O(n) for the dictionary
        freq_dict = dict()
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1
        
        # Time: O(nlogn) (for sorting the dict items), Space: O(n) for the dictionary
        # return [x[0] for x in sorted(list(freq_dict.items()), key = lambda x: x[1], reverse=True)[:k]]

        # Time: O(n) (for creating the dictionary and the list), Space: O(n) for the dictionary and list
        freq_list = [[] for _ in range(len(nums)+1)]

        for num in freq_dict:
            freq_list[freq_dict[num]].append(num)
        
        k_list = []
        pos = -1

        while len(k_list) < k:
            k_list += freq_list[pos]
            pos -= 1
        
        return k_list
