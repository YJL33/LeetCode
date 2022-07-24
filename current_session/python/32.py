class Solution:
    def longestValidParentheses(self, s: str) -> int:     
        # clarification:
        #
        # thoguhts:
        # use a stack
        # append all lefts into the stack
        # when there's a right,
        # check if stack is empty or not
        # if not empty, pop one and calculate the length,
        # and update the longest_parentheses_seen
        # if parentheses closed earlier, add it back later if possible/needed
        #
        # e.g. [()()()())()()]
        #      [0204060800204]       local length
        #      [0224466888888]       longest seen

        left = []       # stack of lefts, store index
        max_seen = 0

        add = [0 for _ in s]
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            else:
                if len(left) > 0:
                    prev = left.pop()
                    local_seen = add[prev-1]+i-prev+1
                    max_seen = max(max_seen, local_seen)
                    add[i] = local_seen
        return max_seen

print(Solution().longestValidParentheses(")()())()()("))
