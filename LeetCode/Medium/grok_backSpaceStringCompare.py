#The trick is to use two pointers starting from the back and on every loop find the next valid character to use. Use a
#a method to find valid character by accounting for the backspace.

#TC = O(M + N) where M and N are the lengths if the two strings and SC = O(1)
def backspaceCompare(self, s, t):

    def get_valid_char(Str, index):
        back_space = 0
        while index >= 0:
            if Str[index] == '#':
                back_space += 1
            elif back_space > 0:
                back_space -= 1
            else:
                break

            index -= 1
        return index

    s_pt = len(s) - 1
    t_pt = len(t) - 1

    while s_pt >= 0 or t_pt >= 0:
        s_index = get_valid_char(s, s_pt)
        t_index = get_valid_char(t, t_pt)

        if s_index < 0 and t_index < 0:
            return True
        if s_index < 0 or t_index < 0:
            return False

        if s[s_index] != t[t_index]:
            return False

        s_pt = s_index - 1
        t_pt = t_index - 1

    return True