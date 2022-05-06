#TC = O(N * 2^N) and SC = O(N * 2^N)

def generateAbbreviations(self, word: str) -> List[str]:

    #index keeps track of which word to add to cur_string, count is the num of abbreviations, cur_string is abbreviated
    #word we want to add to result.
    def abbreviator(word, result, index, count, cur_string):
        # if index is equal to len of word then we have the abbreviated word in cur_string so add to result.
        #if count is greater than 0 add to cur
        if len(word) == index:
            result.append(cur_string + str(count) if count > 0 else cur_string)
        else:
            # we want to abbreviate, increase count to abbreviate the word and increase index to know which word to add
            #when we stop abbreviating.
            abbreviator(word, result, index + 1, count + 1, cur_string)

            # we don't want to abbreviate and add the count and word to the cur string.
            abbreviator(word, result, index + 1, 0, cur_string + (str(count) if count > 0 else '') + word[index])

    result = []
    abbreviator(word, result, 0, 0, "")
    return result