# We need to find the max value of the minimum difference bags. We will need to first find all possibilties
# of combining the cookies a amoung the bags and then find the smallest difference amoung them.

# We will use backtracking to build out all the possible combinations of cookies in the bags. From the combinations we will find the minimum maxinum sum in the bag.

# TC = O(k ^ n) and SC = O(n + k)

class Solution:

    def distributor(self, bags, cookie_index, cookie_num, k, cookies):
        if cookie_index >= cookie_num:
            self.res = min(self.res, max(bags))
            return

        for bag_index in range(k):
            bags[bag_index] += cookies[cookie_index]
            self.distributor(bags, cookie_index + 1, cookie_num, k, cookies)
            bags[bag_index] -= cookies[cookie_index]

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies)

        bags = [0] * k
        self.res = float('inf')

        self.distributor(bags, 0, len(cookies), k, cookies)

        return self.res