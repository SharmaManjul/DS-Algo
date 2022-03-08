#Convert excel column names to column numbers. So pretty much asking to convert
# a base 26 number to decimal. First we will need to convert the characters to
#base 26 number and then convert that do decimal.

def titleToNumber(self, columnTitle):
    result, position = 0, 0

    for letter in reversed(columnTitle):
        digit = ord(letter) - 64
        result += digit * 26**position
        position += 1
    return result
