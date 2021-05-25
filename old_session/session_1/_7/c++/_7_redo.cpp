/* Copyright [2017] <YJLee>
 7. Reverse Integer

    Total Accepted: 203936
    Total Submissions: 860888
    Difficulty: Easy
    Contributors: Admin

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
*/
# include <iostream>
# include <stdlib.h>     /* abs */
# include <climits>

using std::cout;
using std::endl;

class Solution {
 public:
    int reverse(int x) {
        long long int result = 0;
        int remain = abs(x);
        while (remain != 0) {
            result = result*10+remain%10;
            remain = remain/10;
        }
        if (x < 0) result *= -1;
        return (result > INT_MAX || result < INT_MIN) ? 0 : result;
    }
};

int main() {
    int a = 123;
    int b = -123;
    int c = 0;
    std::cout << a << " => " << Solution().reverse(a) << std::endl;
    std::cout << b << " => " << Solution().reverse(b) << std::endl;
    std::cout << c << " => " << Solution().reverse(c) << std::endl;
}
