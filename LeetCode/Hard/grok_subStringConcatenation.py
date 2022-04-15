#Find the indexes of the different way in which words can be combined and exist in s.

#Trick to think a the word level instead of the individual letter level. Most of the code is just to help do that.
def findSubstring(self, s, words):
    if len(s) == 0 or len(words) == 0:
        return []

    w_count = len(words)
    w_length = len(words[0])
    res = []
    w_map = {}

    for word in words: #Load up the frequency hash map.
        if word not in w_map:
            w_map[word] = 0
        w_map[word] += 1

    for i in range((len(s) - w_count * w_length) + 1):# We only want to loop till it is possible to have the words in s.
                                                      # So no point in looping after the difference since the words won't fit in there.
        w_seen = {}
        for j in range(0, w_count):#loop inside for every word length which is the same for all words
            n_index = i + j * w_length #the starting index for each possible word in s based on i
            n_word = s[n_index: n_index + w_length] #get the word from the new index.

            if n_word not in w_map: #if it's not in words just break because no point in doing anything else
                break

            if n_word not in w_seen: #increase seen value for word
                w_seen[n_word] = 0
            w_seen[n_word] += 1

            if w_seen[n_word] > w_map.get(n_word, 0): #if seen is more than the actual map then break as its not a valid combination.
                break

            if j + 1 == w_count: #We will only arrive here when all the words are a valid combination of the words list. store the index and move on.
                res.append(i)

    return res