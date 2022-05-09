# TC = O(N) where N is the number of bits and SC = O(1)

def bitwiseComplement(self, n: int) -> int:
    # Edge case
    if n == 0:
        return 1

    # Count the number of valid bits present in n.
    bit_count = 0
    num = n
    while n > 0:
        bit_count += 1
        n = n >> 1

    # The number which has all bits as 1s will be 2 raised to bit_bount - 1.
    all_bits_set = pow(2, bit_count) - 1

    return num ^ all_bits_set