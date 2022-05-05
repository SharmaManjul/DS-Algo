#TC = roughly O(N * 2^N) and SC = O(N * 2^N)
#Real TC is bounded by the catlan number: O(4^N * sqrt(N)

#Iteratively
class Solution:
    #Class to creat single parenthese objects to help keep track of string and the open and closed parentheses.
    class ParenthesesString:
        def __init__(self, s, opened, closed):
            self.s = s
            self.opened = opened
            self.closed = closed

    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = deque()
        parentheses.append(self.ParenthesesString("", 0, 0))
        result = []

        #Keep looping until all the final parentheses strings have been added the result array.
        while parentheses:
            #Get parentheses string.
            ps = parentheses.pop()

            #If the number of opened and closed is equal tro n then we know the the parentheses is complete.
            if ps.opened == n and ps.closed == n:
                result.append(ps.s)
            else:
                #If opened is less than n then we generate new parentheses with an additional ( appened
                if ps.opened < n:
                    parentheses.append(self.ParenthesesString(ps.s + "(", ps.opened + 1, ps.closed))
                #If closed is less than opened then we generate a new parentheses with and additional )
                if ps.opened > ps.closed:
                    parentheses.append(self.ParenthesesString(ps.s + ")", ps.opened, ps.closed + 1))

        return result

#Recursively
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Initialize finaly parentheses combination size so we can use index to enter in the next parentheses.
        parentheses = [0 for x in range(2 * n)]
        result = []
        self.generator(n, parentheses, result, 0, 0, 0)
        return result

    #Recursive function keeps track of the parentheses string, num of open parentheses, num of closed parentheses and
    #the index at which we would want to add the next parentheses.
    def generator(self, n, parentheses, result, opened, closed, index):
        if opened == n and closed == n:
            result.append(''.join(parentheses))
        else:
            if opened < n:
                parentheses[index] = "("
                self.generator(n, parentheses, result, opened + 1, closed, index + 1)
            if opened > closed:
                parentheses[index] = ")"
                self.generator(n, parentheses, result, opened, closed + 1, index + 1)