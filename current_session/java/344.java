/*
344
*/
class Solution {
    public void reverseString(char[] s) {
        int l = 0, r = s.length-1;
        while (l<r) {
            char tmp = s[r];
            s[r] = s[l];
            s[l] = tmp;
            l += 1;
            r -= 1;
        }
    }
}