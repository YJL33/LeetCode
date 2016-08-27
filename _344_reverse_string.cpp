/*
344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh". 
*/
#include <iostream>
#include <string>
class Solution {
public:
    string reverseString(string s) {
        int i = 0, j = s.size() - 1;
        while(i < j){
            swap(s[i++], s[j--]); 
        }
        
        return s;
    }
};

/*
#include <iostream>
#include <string>
class Solution {
public:
    string reverseString(string s) {
        int length = s.length();
        string res;
        cout << length << endl;
        for (int i = length-1; i>=0; i--) {
            res += s[i];
        }
        return res;
    }
};
*/