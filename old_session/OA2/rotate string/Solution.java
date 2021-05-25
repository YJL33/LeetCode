/*
Rotate String
Problem:
Given two words, find if second word is the round rotation of first word.
For example: abc, cab
return 1
since cab is round rotation of abc

Example2: ab, aa
return -1
since ab is not round rotation for aa
*/
public class Solution {
    public static boolean isRotated(String s, String t)
    {
        if (s == null && t == null) return true;
        else if (s == null || t == null) return false;
        return ((s.length() == t.length()) && ((s+s).indexOf(t) != -1));
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        String s = "abcdef", t = "efabcd";
        System.out.println(isRotated(s, t));
    }
 
}