/*
find optimum weights
(Close two sum)
*/
import java.util.Arrays;
 
class Container {
    public double first;
    public double second;
    public Container(double first, double second)
    {
        this.first = first;
        this.second = second;
    }
}
public class Solution {
    public static Container findOptimalWeights(double capacity, double[] weights)
    {
        if (weights == null || weights.length < 2) return null;
        Arrays.sort(weights);                           // sort the candidates
        if (weights[0] + weights[1] > capacity) return null;
        int l = 0, r = weights.length-1;
        double small = weights[0], big = weights[1];
        while (l < r)
        {
            if (small+big == capacity) break;                   // good
            else if (weights[l] + weights[r] > capacity) r--;   // too big, move to left
            else if (weights[l] + weights[r] > small+big) {     // update the candidates
                small = weights[l];
                big = weights[r];
                l++;
            }
        }
        return new Container(small, big);
    }
    public static void main(String[] args)
    {
        Container res = findOptimalWeights(35, new double[]{10, 24, 30, 9, 19, 23, 7});
        System.out.println("target is 35");
        System.out.println(res.first+" "+res.second);
    }
}