#Find longest substring of k distinct characters.

#Using Sliding window with a hasmap to keep track of characters. Make sure to check max length by end-start instead of
#hash map len. TC = O(n) } O(n+n) since while loop executes once per element and SC=O(n)
def longest_substring_with_k_distinct(str1, k):
    str_map = {}
    w_start=max_len=0

    for w_end in range(len(str1)):
        if str1[w_end] in str_map:
            str_map[str1[w_end]] += 1
        else:
            str_map[str1[w_end]] = 1
        print(str_map)
        while len(str_map) > k:
            max_len = max(max_len, w_end-w_start)
            if str_map[str1[w_start]] > 1:
                str_map[str1[w_start]] -= 1
            else:
                del str_map[str1[w_start]]
            w_start += 1
    return max_len


def main():
  print("Length of the longest substring: "
           + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: "
           + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: "
           + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()