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
        Map<Character, Character> par = new HashMap<Character, Character>();
        par.put('(', ')');
        par.put('[', ']');
        par.put('{', '}');

        for (char c: s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{')
                stack.push(c);
            else if (!stack.empty() && par.get(stack.peek()) == c)
                stack.pop();
            else
                return false;
        }
        return stack.empty();
    }
}
