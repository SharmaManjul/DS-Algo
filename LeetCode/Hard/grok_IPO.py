#TC =O(P*logP + C*logC)
#SC= O(C)

def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    min_capital = []
    max_profit = []

    #Create min heap of all the capital since we want the least amount of capital required.
    for i in range(len(capital)):
        heapq.heappush(min_capital, (capital[i], i))

    available_capital = w

    #O(P *logP + C * logC): since in worst case all in min_capital will be less than available to that part will be C*logC
    #then the number of projects will keep looping until over adn popping profits which will be P*logP

    #Loop through project numbers and for every capital less than the available enter profit into max heap once done pop
    #the max heap to get the max profit possible and add to available heap and return until number of projetcs is done.
    #Break the loop if the max profit heap is empty.
    for _ in range(k):
        # C * logC
        while min_capital and min_capital[0][0] <= available_capital:
            cur_capital, index = heapq.heappop(min_capital) #O(logC)
            heapq.heappush(max_profit, -profits[index]) #O(logC)

        if not max_profit:
            break

        available_capital += -heapq.heappop(max_profit) #O(log)

    return available_capital
