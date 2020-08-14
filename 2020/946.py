"""
946. Validate Stack Sequences

Given two sequences pushed and popped with distinct values,
return true if and only if this could have been the result of 
a sequence of push and pop operations on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Constraints:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.

"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # naive approach
        # maintain 2 cursors and one queue
        # time: O(2n)
        # space: O(n)

        i, j = 0, 0
        prev = []
        while i < len(pushed):
            if pushed[i] != popped[j] and (prev == [] or popped[j] != prev[-1]):
                # print "push:", pushed[i], prev
                prev += pushed[i],
                i += 1
            elif prev != [] and popped[j] == prev[-1]:
                j += 1
                prev.pop()
            elif pushed[i] == popped[j]:
                # print "push and pop:", popped[j]
                i, j = i+1, j+1
            else:
                return False

        while j < len(popped) and prev != [] and popped[j] == prev[-1]:
            # print "pop:", popped[j], prev[-1]
            j += 1
            prev.pop()

        return (i == len(pushed) and j == len(popped))

print Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]), "T"
print Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2]), "F"
print Solution().validateStackSequences([1,2,3,4,5], [3,5,4,2,1]), "T"
print Solution().validateStackSequences([1,2,3,4,5], [5,4,3,2,1]), "T"
print Solution().validateStackSequences([1,2,3,4,5], [1,3,2,5,4]), "T"
print Solution().validateStackSequences([1,2,3,4,5], [1,3,5,4,2]), "T"
print Solution().validateStackSequences([1,2,3,4,5], [1,3,5,2,4]), "F"
