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

