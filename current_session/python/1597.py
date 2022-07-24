# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # clarification:
    # upperbound/lowerbound of node value? operands are only one digit
    # restrictions on memory/timeout?
    #
    # solutions:
    # 1. direct conversion
    # handle brackets first, use helper function
    # (due to the nature of infix, it too complicated and error-prone.)
    #
    # 2. infix -> postfix -> binary expression tree
    # convert in-fix to post-fix notation, and then craft binary expression tree by post-fix notation.
    #
    # tc: O(n) conversion, O(n) craft the tree
    # sc: O(n) to output the tree, O(h) where h is the height of stack in both pass. (worst case O(n))
    # 
    # dummy cases:
    # e.g. 1+3-2 -> 13+2-    1+(3-2) -> 132-+   1+2*3 -> 123*+   "2-3/(5*2)+1" -> 2352*/1+-
    # detail implementation provided below
    def expTree(self, s: str) -> 'Node':
        # convert infix to postfix
        # from left to right, whenever we see operators, put it into stack
        # check the priority of operator and output "*/" before '+-'
        # bracket has priority == 0, using as a wall
        # maintain a monotonic increasing stack in operator priority, but separated by 0.
        # (so that we will output in a decreasing order)
        def _infix_to_postfix(s):
            # print('input:', s)
            output, op_stack, priority = [], [], {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}
            for c in s:
                if c.isdigit():
                    output.append(c)
                else:
                    if c == '(':
                        op_stack.append(c)
                    elif c == ')':
                        while op_stack and op_stack[-1] != "(":
                            output.append(op_stack.pop())
                        op_stack.pop()
                    elif op_stack and priority[c] > priority[op_stack[-1]]:
                        op_stack.append(c)
                    else:
                        while op_stack and op_stack[-1] != '(':
                            output.append(op_stack.pop())
                        op_stack.append(c)
                # print('op_stack', [priority[c] for c in op_stack])
            while op_stack:
                output.append(op_stack.pop())
            # print('output', ''.join(output))
            return output
        
        # craft the nodes based on postfix notation
        # stash nodes in the stack and craft the node
        # (post-order traversal, left-right-root)
        def _build_bet_by_postfix(postfix):
            node_stack = []
            for c in postfix:
                if c not in '+-*/':
                    node_stack.append(Node(c))
                else:
                    r = node_stack.pop()
                    l = node_stack.pop()
                    node_stack.append(Node(c, l, r))
            return node_stack[-1]
            
        postfix = _infix_to_postfix(s)
        root = _build_bet_by_postfix(postfix)
        
        return root