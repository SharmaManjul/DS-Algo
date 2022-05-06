#TC = O(log N) and SC = O(1)

def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    letters_len = len(letters)
    start, end = 0, letters_len - 1

    # if the target is less than first letter or greater than lat letter return the first letter.
    if target < letters[start] or target > letters[end]:
        return letters[start]

    while start <= end:

        mid = start + (end - start) // 2

        # We only need to check if target is less than the mid or else increament start since if the target is greater than
        # mid and if it is equal to mid we need to increament start. When target equal to mid, start will be at the ideal position.
        if target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return letters[start % letters_len]