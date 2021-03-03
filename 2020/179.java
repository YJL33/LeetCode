import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String largestNumber(int[] nums) {
        List<String> arr = Arrays.stream(nums).mapToObj(i -> ((Integer) i).toString()).collect(Collectors.toList());
        arr.sort((String s1, String s2) -> (s2+s1).compareTo(s1+s2));
        // regex: find one or more leading zeros if not followed by the end of string
        return String.join("", arr).replaceAll("^0+(?!$)", "");
    }
}