#TC=O(log N) and SC=O(1)
def squared_sum(self, num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit * digit
        num /= 10
    return sum


def isHappy(self, n):
    fast, slow = n, n
    while True:
        slow = self.squared_sum(slow)
        fast = self.squared_sum(self.squared_sum(fast))
        if fast == slow:
            break
    return slow == 1