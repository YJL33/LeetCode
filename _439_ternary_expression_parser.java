/*
439. Ternary Expression Parser

Given a string representing arbitrarily nested ternary expressions,
calculate the result of the expression.
You can always assume that the given expression is valid and only consists of digits 0-9, ?, :,
T and F (T and F represent True and False respectively).

Note:

The length of the given string is <= 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.

*/
public class Solution {
    public String parseTernary(String expression) {
        while (expression.length() != 1) {
            int i = expression.lastIndexOf("?");    // get the last shown '?'
            char tmp;
            if (expression.charAt(i-1) == 'T') { tmp = expression.charAt(i+1); }
            else { tmp = expression.charAt(i+3); }
            expression = expression.substring(0, i-1) + tmp + expression.substring(i+4);
        }
        return expression;
    }
}