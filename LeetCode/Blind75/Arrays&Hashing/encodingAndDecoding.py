# The trick is to use the length of the word and a # as the divider for the word when combined into string. The lenght
# will let the decoder know till when to loop and grab valid character and the # will let the decoder know when to start
# the looping. This way the word can have any charcaters and we will still know when they start and end by using this
# divider combination.

class Codec:
    # O(N)
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = []

        # Adding a number to indicate length and then a divider symbol. So when we encounter this
        # we will know for sure that our word is some length and start after divider symbol.
        for word in strs:
            encoded_str.append(str(len(word)) + '#' + word)

        return "".join(encoded_str)

    # O(N)
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_list, i = [], 0

        while i < len(s):
            j = i
            # We want to find the divider symbol but we will need to loop because the lenght could
            # be multiple digits.
            while s[j] != '#':
                j += 1
            # Convert the number before the divider to int to get the upcoming word length.
            word_length = int(s[i:j])
            # Word will start at index after the divider and end divider index plus the word len.
            decoded_list.append(s[j + 1: j + 1 + word_length])
            # Update i to the index after the word end.
            i = j + 1 + word_length

        return decoded_list