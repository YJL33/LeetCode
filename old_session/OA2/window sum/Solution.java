/*
Window Sum
*/
import java.util.*;
public class Solution {
    public static List<Integer> windowSum(List<Integer> input, int k)
    {
        List<Integer> res = new ArrayList<Integer>();
        int localsum = 0;
        for (int i = 0; i < k; i++)
        {
            localsum += input.get(i);
        }
        res.add(localsum);
        for (int j = k; j < input.size(); j++)
        {
            localsum += (input.get(j) - input.get(j-k));
            res.add(localsum);
        }
        return res;
    }
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        List<Integer> input = new ArrayList<>();
        input.addAll(Arrays.asList(2,3,4,2,5,7,8,9,6));
//      List<Integer> input1 = new ArrayList<>();
//      input1.addAll(Arrays.asList(1,2));
        List<Integer> output = windowSum(input, 4);
        for(int i: output) System.out.print(i + " ");
        System.out.print("\n");
    }
 
}
