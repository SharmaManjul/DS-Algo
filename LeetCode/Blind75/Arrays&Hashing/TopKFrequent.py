# Sub optimal solution using hashmap and max heap => O(N.logK) Optimal solution using a hash map to store frequences and
# a frequency list with its index as the freq and elements as the list of nums associated to that frequency. Loop backwards
# to get k freq elements => O(N)
# TC = O(N) and SC = O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()
        freq_list = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        for num, freq in freq_map.items():
            freq_list[freq].append(num)

        result = []

        for freq in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[freq]:
                result.append(num)
                if len(result) == k:
                    return result