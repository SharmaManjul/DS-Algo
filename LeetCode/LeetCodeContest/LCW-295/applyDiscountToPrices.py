# Trick is to know how to use string format to control the decimals and type. We need to check if the word is a valid price
# and we can do so by chekcing if it starts with $ and only contains number till it's end.
# TC = O(N) and SC = O(N)

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        res = []
        for word in words:
            if word[0] != '$' or not word[1:].isnumeric():
                res.append(word)
            else:
                num = int(word[1:])
                res.append("${:.2f}".format(num - (num * (discount / 100))))
        return " ".join(res)