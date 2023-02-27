# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def evaluate(num1: int, num2: int, opp: str) -> int:
            if opp == '+':
                return num1 + num2
            if opp == '-':
                return num1 - num2
            if opp == '*':
                return num1 * num2
            else:
                return num1 / num2

        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                ans = evaluate(num1, num2, token)
                stack.append(ans)

        return int(stack[0])
    
# OR

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        evals = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

        for token in tokens:
            if token not in '+-*/':
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(evals[token](num1, num2))

        return int(stack[0])
    
# OR 

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token is '+':
                    ans = num1 + num2
                if token is '-':
                    ans = num1 - num2
                if token is '*':
                    ans = num1 * num2
                if token is '/':
                    ans = num1 / num2

                stack.append(ans)

        return int(stack[0])

#==============================================================================================================

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
#     Input: digits = [1,2,3]
#     Output: [1,2,4]
#     Explanation: The array represents the integer 123.
#     Incrementing by one gives 123 + 1 = 124.
#     Thus, the result should be [1,2,4].

# Example 2:
#     Input: digits = [4,3,2,1]
#     Output: [4,3,2,2]
#     Explanation: The array represents the integer 4321.
#     Incrementing by one gives 4321 + 1 = 4322.
#     Thus, the result should be [4,3,2,2].

# Example 3:
#     Input: digits = [9]
#     Output: [1,0]
#     Explanation: The array represents the integer 9.
#     Incrementing by one gives 9 + 1 = 10.
#     Thus, the result should be [1,0].
    
# Constraints:
#     1 <= digits.length <= 100
#     0 <= digits[i] <= 9
#     digits does not contain any leading 0's.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        idx = -1
        digits[idx] += 1

        while digits[idx] > 9:
            digits[idx] = 0
            if len(digits) > -idx:
                digits[idx - 1] += 1
                idx -= 1
            else:
                digits.insert(0,1)
            
        return digits