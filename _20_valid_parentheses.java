/*
20. Valid Parentheses

    Total Accepted: 138038
    Total Submissions: 443232
    Difficulty: Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
*/
public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        int cur = 0;
        boolean isCorrect = true;
        while (cur < s.length() && isCorrect) {
        	if (s.charAt(cur) == '(' || s.charAt(cur) == '[' || s.charAt(cur) == '{') {
        		stack.push(s.charAt(cur));
        	}
            else if(s.charAt(cur) == ')' && !stack.empty() && stack.peek() == '(')
                stack.pop();
            else if(s.charAt(cur) == ']' && !stack.empty() && stack.peek() == '[')
                stack.pop();
            else if(s.charAt(cur) == '}' && !stack.empty() && stack.peek() == '{')
                stack.pop();
            else
                return false;
            cur++;
        }
        return stack.empty();
    }
}
