from typing import List
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # return the account name -> rest of emails in sorted order
        # keep two dict
        # 1st:
        # key = mail, value = list of (index of account)
        # use DFS
        mailDct = collections.defaultdict(list)
        for i in range(len(accounts)):
            a = accounts[i]
            mails = a[1:]
            for m in mails:
                mailDct[m].append(i)

        # helper - dfs
        visited = [False for _ in accounts]    
        def dfs(i, emails):
            if visited[i]: return
            visited[i] = True
            for m in accounts[i][1:]:
                emails.add(m)
                for nb in mailDct[m]:       # handle neighbors
                    dfs(nb, emails)
            return emails

        ans = []
        for i in range(len(accounts)):
            if visited[i]: continue
            emails = set()
            dfs(i, emails)
            ans += [accounts[i][0]]+sorted(emails),

        return ans

        