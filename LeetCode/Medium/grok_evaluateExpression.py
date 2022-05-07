#TC = O(N * 2^N) and SC = O(2 ^ N)

def diffWaysToCompute(self, expression: str) -> List[int]:
    results = []

    # If expression only has number then append number to result and return, no need to do any operation since none exist.
    if '-' not in expression and '+' not in expression and '*' not in expression:
        results.append(int(expression))
    else:
        # Loop through the entire expression.
        for i in range(len(expression)):
            # Keep track of every char, since this will let us know the operation to perform.
            char = expression[i]

            # Check if current char is an operation.
            if not char.isdigit():
                # Split into two parts and evaluate them separately.
                left_part = self.diffWaysToCompute(expression[0:i])
                right_part = self.diffWaysToCompute(expression[i + 1:])

                # After the recursive stack begins to resolve some left elements will have multiple right elements to
                # perform the operation on since we are looking for all the combinations. So we loop through all the right
                # for every left.
                for left in left_part:
                    for right in right_part:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        if char == '*':
                            results.append(left * right)

    return results