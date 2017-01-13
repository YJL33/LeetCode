/*
remove vowel
*/
import java.util.*;
public class Solution {
    public static String removeVowel(String s)
    {
        char[] chars = s.toCharArray();
        StringBuilder res = new StringBuilder();
        Set<Character> h = new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        for (char c : chars)
        {
            if (!h.contains(c)) res.append(c);
        }
        return res.toString();

    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        System.out.println(removeVowel("abcdefghijk"));
    }
 
}
