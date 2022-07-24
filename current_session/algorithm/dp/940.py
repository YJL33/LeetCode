import collections
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        return    

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # use DP bottom-up
        # leverage Trie
        # for all possible sub-strings, insert the sub-string into the Trie
        # if not exist: add it and count
        # in the end, count the number of words

        # time analysis: O(X), where X is the number of all possible substrings, propotional to N!
        # space analysis: O(X), where X is the number of all possible substrings, propotional to N!

        # self.root = Node()
        # self.cnt = 0
        # L = len(s)
        
        # def find_substring(node, lastend):
        #     for i in range(lastend+1, L):
        #         if s[i] not in node.children:
        #             node.children[s[i]] = Node()
        #             self.cnt += 1
        #             find_substring(node.children[s[i]], i)
        #     return
        
        # find_substring(self.root, -1)   
        # return self.cnt%1000000007

        # only count the number of the substring ending with this number
        # time analysis: O(N*26)
        # space analysis: O(N*26)
        end = [0]*26
        for c in s:
            end[ord(c)-ord('a')] = sum(end)+1
        return sum(end) % (10**9+7)
                