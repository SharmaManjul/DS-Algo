#TC = O(N * N^2) and SC = O(N * N^2)

def letterCasePermutation(self, s: str) -> List[str]:
    permutations = []
    permutations.append(s)
    #Loop through all the single characters in the string.
    for i in range(len(s)):
        p_len = len(permutations)
        #For each character add a capitalized version of the permutation to the permutations list.
        for j in range(p_len):
            if s[i].isalpha():
                new_permutation = list(permutations[j])
                new_permutation[i] = new_permutation[i].swapcase()
                permutations.append(''.join(new_permutation))

    return permutations