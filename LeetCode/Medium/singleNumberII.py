# TC = O(N) and SC = O(1)

def singleNumber(self, nums: List[int]) -> int:
    # Since we know all nums except one repeat 3 times that means that if we keep a count of all
    # individual 32 bits all of them should add up to 3 expect the ones that represent the missing
    # num.

    res = 0

    # Start a loop till 32, so we check the same bit of every num.
    for i in range(32):

        # For every bit loop thorugh all the nums. Use a temp var to store the shifted num by i.
        # We want it shifted by i as we will bitwise & it with 1 and store the val in temp. Temp will
        # now tell us if the bit at the index is either 1 or 0 and we can add that to the count.
        count = 0
        for num in nums:
            temp = num >> i
            temp = temp & 1
            count += temp

        missing_bit = count % 3

        # Now we have the bit based on if it repeated 3 times or not.

        # If i == 31 and the missing_bit is 1, this means that our missing num is -ve so we need to
        # adjust for it by subtracting our result with the numbe that is represented by the most
        # significant bit.
        if i == 31 and missing_bit:
            res -= 1 << 31

        # Else we want to put the value of the missing bit where it belongs (ie shifted by i) in the
        # res.
        else:
            res |= missing_bit << i

    return res