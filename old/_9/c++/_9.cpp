/*
 9. Palindrome Number

    Total Accepted: 179846
    Total Submissions: 528632
    Difficulty: Easy
    Contributors: Admin

Determine whether an integer is a palindrome.
Do this without extra space.
*/
# include <iostream>
# include <vector>

using std::vector;
using std::cout;
using std::endl;

class Solution {
 public:
    bool isPalindrome(int num) {
        // reverse half
        if (num < 0 || (num != 0 && num % 10 == 0)) return false;
        int sum = 0;
        while (num > sum) {
            sum = sum * 10 + num % 10;
            num = num / 10;
        }
        return (num == sum) || (num == sum/10);
    }
};
int main() {
    Solution sol = Solution();
    std::cout << 1874994781 << " => " << sol.isPalindrome(1874994781) << std::endl;
    std::cout << 1224 << " => " << sol.isPalindrome(1224) << std::endl;
}
