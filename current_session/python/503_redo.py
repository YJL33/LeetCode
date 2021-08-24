
class Solution:
    def nextGreaterElements(self, A):
        if not A: return []
        maxVal = max(A)
        st = []
        res = [-1 for _ in A]
        for i in range(len(A)):
            while st and A[i] > A[st[-1]]:
                res[st.pop()] = A[i]
            if A[i] < maxVal: st.append(i)
        
        for j in range(len(A)):
            if not st: break
            while st and A[j] > A[st[-1]]:
                res[st.pop()] = A[j]

        return res

print(Solution().nextGreaterElements([1,2,3,4,3]))
