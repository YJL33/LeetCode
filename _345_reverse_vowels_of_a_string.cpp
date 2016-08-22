/*
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
*/
class Solution {
public:
string reverseVowels(string s) {
    string s1=s;
    int n= s1.length();
    int i=0,j=n-1;
    while(i<j) {
        while((!isVovel(s1[i]))&&i<j)i++;
        while((!isVovel(s1[j]))&&i<j)j--;
        swap(s1[i],s1[j]);
        i++;j--;
        }
    return s1;
    }
private:
bool isVovel(char &ch) {
    bool flag=false;
    if((ch=='a')||(ch=='e')||(ch=='i')||(ch=='o')||(ch=='u')
    ||(ch=='A')||(ch=='E')||(ch=='I')||(ch=='O')||(ch=='U'))
        flag = true;
    return flag;
    }
};