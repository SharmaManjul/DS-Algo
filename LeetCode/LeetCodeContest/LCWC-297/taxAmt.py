# TC = O(N) and SC = O(1)

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = float(0)
        prev_bracket = 0

        for bracket in brackets:
            amt_to_be_taxed = bracket[0] - prev_bracket
            if income >= amt_to_be_taxed:
                taxes += (amt_to_be_taxed * bracket[1]) / 100
                income -= amt_to_be_taxed
                prev_bracket = bracket[0]
            else:
                taxes += (income * bracket[1]) / 100
                break

        return taxes