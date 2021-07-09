"""
721
"""
import collections
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # return the account name -> rest of emails in sorted order
        # keep two dict
        # 1st:
        # key = mail, value = list of (index of account)
        # 2nd:
        # key = index of account, value = list of mails
        mailDct = collections.defaultdict(list)
        for i in range(len(accounts)):
            a = accounts[i]
            mails = a[1:]
            for m in mails:
                mailDct[m].append(i)

        # helper - dfs
        visited = [False for _ in accounts]    
        def helper(i, emails):
            if visited[i]: return
            visited[i] = True
            for m in accounts[i][1:]:
                emails.add(m)
                for nb in mailDct[m]:       # handle neighbors
                    helper(nb, emails)
            return emails

        ans = []        
        for i in range(len(accounts)):
            if visited[i]: continue
            emails = set()
            helper(i, emails)
            ans += [accounts[i][0]]+sorted(emails),

        return ans


print(Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
