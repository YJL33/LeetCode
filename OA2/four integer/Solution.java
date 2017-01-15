/*
four integer
*/
import java.util.Arrays;
 
public class Solution {
    public static int[] fourInteger(int a, int b, int c, int d)
    {
        int[] res = new int[]{a, b, c, d};
        Arrays.sort(res);
        return new int[]{res[2], res[0], res[3], res[1]};
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int[] nums = fourInteger(1, 3, 2, 4);
        for(int i: nums) System.out.print(i + " ");
    }
 
}