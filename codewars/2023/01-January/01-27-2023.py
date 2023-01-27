# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# Return the array after sorting it.

# Example 1:
#     Input: arr = [0,1,2,3,4,5,6,7,8]
#     Output: [0,1,2,4,8,3,5,6,7]
#     Explantion: [0] is the only integer with 0 bits.
#     [1,2,4,8] all have 1 bit.
#     [3,5,6] have 2 bits.
#     [7] has 3 bits.
#     The sorted array by bits is [0,1,2,4,8,3,5,6,7]

# Example 2:
#     Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
#     Output: [1,2,4,8,16,32,64,128,256,512,1024]
#     Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
 
# Constraints:
#     1 <= arr.length <= 500
#     0 <= arr[i] <= 104

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key = lambda num: (bin(num).count('1'), num))

#==============================================================================================================

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
# Example 1:
#     Input
#         ["MyQueue", "push", "push", "peek", "pop", "empty"]
#         [[], [1], [2], [], [], []]
#     Output
#         [null, null, null, 1, 1, false]
#     Explanation
#         MyQueue myQueue = new MyQueue();
#         myQueue.push(1); // queue is: [1]
#         myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
#         myQueue.peek(); // return 1
#         myQueue.pop(); // return 1, queue is [2]
#         myQueue.empty(); // return false
 

# Constraints:
#     1 <= x <= 9
#     At most 100 calls will be made to push, pop, peek, and empty.
#     All the calls to pop and peek are valid.

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
        
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

#==============================================================================================================

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
#     Input: s = "anagram", t = "nagaram"
#     Output: true

# Example 2:
#     Input: s = "rat", t = "car"
#     Output: false
 
# Constraints:
#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# OR

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_count, t_count = {}, {}
        for idx in range(len(s)):
            s_count[s[idx]] = s_count.get(s[idx], 0) + 1
            t_count[t[idx]] = t_count.get(t[idx], 0) + 1

        
        return s_count == t_count

#==============================================================================================================