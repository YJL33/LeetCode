#include <iostream>
#include <vector>

using namespace std;

// use bottom up dp
// dp[i][k] = solution of A[:i] with k
// dp[n+1][1] = solution of A[:n+1] with k=1 (avg of A[:n+1])
// dp[n+1][2] = solution of A[:n+1] + avg of A[n+1:]
//              = dp[n+1][1] + sum(A[n+1:])/cnt
// time complexity: O(k*n^2)

class Solution {
public:
    double dp[200][200];
    double largestSumOfAverages(vector<int>& A, int K) {
        memset(dp, 0, sizeof(dp));      // initialize the array
        int N = A.size();
        double cur = 0;
        for (int i=0; i<N; ++i) {       // create dp[][1]
            cur += A[i];
            dp[i+1][1] = cur/(i+1);
        }
        return search(N, K, A);
    }

    double search(int n, int k, vector<int>& A) {
        if (dp[n][k] > 0) return dp[n][k];
        if (n<k) return 0;                  // 14ms to 10ms
        double cur = 0;
        double localSol = 0;
        for (int i= n-1; i>0; --i) {
            cur += A[i];
            localSol = max(localSol, search(i, k-1, A) + cur/(n-i));
        }
        dp[n][k] = localSol;
        return dp[n][k];
    }
};