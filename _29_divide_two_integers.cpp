/*
29. Divide Two Integers

    Total Accepted: 78327
    Total Submissions: 491995
    Difficulty: Medium

Divide two integers without using multiplication,
division and mod operator.

If it is overflow, return MAX_INT.
*/

class Solution {
public:
    int divide(int dividend, int divisor) {
        // Corner cases.
        // 1. divisor == 0
        // 2. dividend == INT_MIN
        if (!divisor || (dividend == INT_MIN && divisor == -1))
            return INT_MAX;
        int sign = ((dividend > 0) == (divisor > 0));
        // looking for a/b
        long long a = labs(dividend);    // denominator
        long long b = labs(divisor);     // numerator
        int res = 0;
        while (a >= b) { 
            long long temp = b, multiple = 1;
            while (a >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            a -= temp;
            res += multiple;
        }
        return sign ? res : -res; 
    }
};