# TC = O(N) and SC = O(1) where N is all the elements in the matrix.

def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    l = len(image)
    # Loop through entire matric and swap the two numbers while calculating their compliment. Since swap is done thorugh
    # temp variable under the hood, even if we are swapping the same number the result is still the compliment of the original.
    for i in range(l):
        for j in range((l + 1) // 2):
            k = l - j - 1
            image[i][j], image[i][k] = image[i][k] ^ 1, image[i][j] ^ 1

    return image