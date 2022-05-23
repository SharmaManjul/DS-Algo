# Trick is to realize that for all anangrams the number of charcters will always be the same. So maintain a char freq
# list (len 26) and update it by subtracting ascii of a from the letter to get list index. Store the list as a tuple in
# hash map and store the words in a list as values of the key.
# TC = O(N*M*26) = O(N*M) where N is num of words and M is the length of the words, SC = O(N*26) = O(N)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count_map = defaultdict(list)

        for word in strs:
            char_count = [0] * 26

            for char in word:
                char_count[ord(char) - ord('a')] += 1

            char_count_map[tuple(char_count)].append(word)

        return char_count_map.values()