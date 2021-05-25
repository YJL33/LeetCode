/*
Arithmetic Sequence
find out number of arithmetic sequence in array, if result > 1 billion return -1.
[0,1,2,3,2,1] -> 4 ({0 ,1, 2},{1, 2, 3},{0, 1, 2, 3},{3, 2, 1})
*/
public class Solution {
    public static int count(int[] input)
    {
        if (input == null || input.length < 3) return 0;
        int diff = input[1]-input[0], seq = 1, res = 0;
        for (int i = 2; i < input.length; i++)
        {
            if (diff == input[i] - input[i-1]) seq++;
            else
            {
                diff = input[i] - input[i-1];
                res += seq*(seq-1)/2;       // if seq > 44721 => return -1
                seq = 1;
            }
        }
        return (res+(seq*(seq-1)/2) > 1000000000) ? -1 : res+(seq*(seq-1)/2);
    }
    public static void main(String[] args)
    {
        int[] input = {0, 1, 2, 3, 4, 5, 4, 3, 2, 1};
        System.out.println(count(input));
    }
}