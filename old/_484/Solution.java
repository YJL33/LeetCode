/*
484. Find Permutation

    User Accepted: 182
    User Tried: 294
    Total Accepted: 188
    Total Submissions: 587
    Difficulty: Medium

By now, you are given a secret signature consisting of character 'D' and 'I'.
'D' represents a decreasing relationship between two numbers,
'I' represents an increasing relationship between two numbers.
And our secret signature was constructed by a special integer array,
which contains uniquely all the different number from 1 to n
(n is the length of the secret signature plus 1).
For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2],
but won't be constructed by array [3,2,4] or [2,1,3,4],
which are both illegal constructing special string that can't represent the "DI" secret signature.

On the other hand,
now your job is to find the lexicographically smallest permutation of [1, 2, ... n]
could refer to the given secret signature in the input.

Example 1:

Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I",
where the number 1 and 2 construct an increasing relationship.

Example 2:

Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation,
you need to output [2,1,3]

Note:
The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000
*/
public class Solution {
    public static int[] findPermutation(String s) {
        // first generate the desired array
        int[] res = new int[s.length()+1];
        for (int i=0; i < s.length()+1; i++) {res[i] = i+1;}
        // check the string from beginning.
        int j = 0;
        while (j < s.length())
        {
            if (s.charAt(j) == 'I') j++;
            else
            {
                int head = j, tail = j;
                // find the continual 'D' in s
                while (tail+1 < s.length() && s.charAt(tail+1) == 'D') tail++;
                // System.out.println(head);
                // System.out.println(tail);
                j = tail+1;
                int temp = 0;
                while (tail+1 > head)
                {
                    // System.out.println("swapping..");
                    temp = res[head];
                    res[head] = res[tail+1];
                    res[tail+1] = temp;
                    tail--;
                    head++;
                }
                for (int i: res) System.out.print(i);
                // System.out.println();
            }
        }
        return res;
    }
    public static void main(String[] args) {
        String inp = "DDIDDIIDI";
        int[] ans = findPermutation(inp);
        for (int i : ans)
        {
            System.out.print(i);
        }
    }
}