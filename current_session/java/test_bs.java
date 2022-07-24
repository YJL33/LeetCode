import java.util.*;
class Solution {
    // cp test_bs.java Solution.java && javac Solution.java && java Solution
    public static void main(String[] args) {
        int[] test1 = {2,3,4,5,6,7};
        int[] test2 = {3,3,3,3,3,3,3,3};
        int[] test3 = {3,3,3,3,3};
        
        int ans1 = Arrays.binarySearch(test1,4);
        int ans2 = Arrays.binarySearch(test2,3);
        int ans3 = Arrays.binarySearch(test3,3);
        
        System.out.println(ans1 + " ??");
        System.out.println(ans2 + " ??");
        System.out.println(ans3 + " ??");
    }
}