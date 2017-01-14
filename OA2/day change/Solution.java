/*
Day change
Given an array and number of days.

Rules: if arr[i-1] == arr[i+1], arr = 0 else arr = 1,
do that for n days.

Code:
can not infer from problem whether input array only contains 1s and 0s, so preprocess.
*/
public class Solution {
    public static int[] dayChange(int[] input, int day)
    {
        if (input == null || input.length == 0 || day <= 0) return input;
        int[] res = new int[input.length];
        for (int j = 0; j < input.length; j++) res[j] = input[j];
        for (int d = 0; d < day; d++)
        {
            for (int i = 1; i < res.length-1; i++)
            {
                res[i] += ((res[i-1]&1) == (res[i+1]&1)) ? 0 : 2;
            }
            for (int i = 0; i < res.length; i++) res[i] >>= 1;
        }
        return res;
    }


    public static int[] dayChange2(int[] input, int day)
    {
        if(input == null || input.length == 0 || day <= 0) return input;
        for(int k = 0; k < day; k++)
        {
            for(int i = 0; i < input.length; i++)
            {
                if(i - 1 >= 0 && i + 1 < input.length && (input[i - 1] & 1) != (input[i + 1] & 1)) input[i] += 2;
            }
            for(int i = 0; i < input.length; i++) input[i] >>= 1;
        }
        return input;
    }


    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int[] input = {1,0,0,0,0,1,0,0};
        int[] output = dayChange(input, 4);
        int[] output2 = dayChange2(input, 4);
        for(int i: output) System.out.print(i);
        System.out.println("");
        for(int i: output2) System.out.print(i);
        System.out.println("");
    }
 
}