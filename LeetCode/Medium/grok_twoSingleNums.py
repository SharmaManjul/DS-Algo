#TC = O(N) and SC = O(1)

def singleNumber(self, nums: List[int]) -> List[int]:
    # Find the the xor of nums to get the xor of n1 and n2
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # Use the fact that a bit in the xor ie n1xn2 is 1 which means that that specifc bit in
    # n1 and n2 is different. Store the bit and its place using bit shifting.
    rightmost_bit = 1
    while (n1xn2 & rightmost_bit) == 0:
        rightmost_bit = rightmost_bit << 1

    # Loop through num and perform bit wise & on every num and rightmost_bit. Keep xoring into
    # different variables based on if the & was a 0 or 1 and at the end we will be left with the
    # two missing nums in the two variables.
    num1, num2 = 0, 0
    for num in nums:
        # All the other numbers will zero out and we will only be left with two nums (num1 and num2)
        # where the rightmost bit for them is different ie either 1 or 0.
        if (num & rightmost_bit) != 0:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]