/*
 * @lc app=leetcode id=72 lang=cpp
 *
 * [72] Edit Distance
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        if (word1.size() == 0 && word2.size() == 0) return 0;
        if (word1.size() == 0) return word2.size();
        if (word2.size() == 0) return word1.size();

        int A = word1.size(), B = word2.size();
        vector<vector<int>> dp(A+1, vector<int>(B+1, 0));
        for (int i = 0; i <= A; ++i) {
        for (int j = 0; j <= B; ++j) {
            if (i==0 && j==0) {
                dp[i][j] = 0;               // edge case
            } else if (i == 0) {
                dp[i][j] = dp[i][j-1]+1;    // insert/delete
            } else if (j == 0) {
                dp[i][j] = dp[i-1][j]+1;    // insert/delete
            } else if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];    // as same as (w1[i-2], w2[j-2])
            } else {
                dp[i][j] = min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]})+1; // min from replace, insert
            }
        }
        }
        return dp[A][B];
    }
};
// @lc code=end

