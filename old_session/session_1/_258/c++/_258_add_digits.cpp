/* [Copyright] <2017> YJLee
 258. Add Digits
Description Submission Solutions Add to List

    Total Accepted: 148844
    Total Submissions: 295667
    Difficulty: Easy
    Contributors: Admin

Given a non-negative integer num,
repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
Since 2 has only one digit, return it.
*/

class Solution {
 public:
    int addDigits(int num) {
        if (num == 0) {
            return 0;
        }
        if (num % 9) {
            return num%9;
        }
        else {
            return 9;
        }
    }
};