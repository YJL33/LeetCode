/*
LRU Cache Count Miss
*/
import java.util.ArrayList;
public class Solution {
    public static int countMiss(int[] input, int size)
    {
        ArrayList<Integer> cache = new ArrayList<>();
        int count = 0;
        for (int i = 0; i < input.length; i++) {
            if (cache.contains(input[i])) cache.remove(new Integer(input[i]));
            if (cache.size() == size) {
                cache.remove(0);
                count++;
            }
            cache.add(input[i]);
        }
        return count;
    }
    // public static int countMiss2(int[] arr, int size)
    // {
    //     if(arr == null || arr.length == 0) return 0;
    //     if(size < 1) return arr.length;

    //     int missed = 0;
    //     LinkedHashMap<Integer, Boolean> cache = new LinkedHashMap<Integer,Boolean>(size, 0.75f, true){
    //         @Override
    //         public boolean removeEldestEntry(Map.Entry<Integer, Boolean> eldest){
    //             return this.size() > size;
    //         }
    //     };
    //     for(int x : arr){
    //         if(cache.get(x) == null){
    //             missed++;
    //             cache.put(x, true);
    //         }
    //     }
    //     return missed;
    // }
         
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int[] input = {1, 1, 3, 4, 5, 6, 1, 3, 8, 1, 3, 4, 5, 1};
        //                x  x  x  x  x        x           should be 6!
        System.out.println(countMiss(input, 4));
        // System.out.println(countMiss2(input, 4));
    }
}
