/*
high five
*/
import java.util.*;
class Result{
    int id;
    int value;
    public Result(int id, int value){
        this.id = id;
        this.value = value;
    }
}
public class Solution {
    public static Map<Integer, Double> getHighFive(Result[] results)
    {
        Map<Integer, PriorityQueue<Integer>> scores = new HashMap<Integer, PriorityQueue<Integer>>();
        for (Result r : results) {
            scores.putIfAbsent(r.id, new PriorityQueue<Integer>(5));    // min heap
            scores.get(r.id).add(r.value);
            if (scores.get(r.id).size() > 5) scores.get(r.id).poll();
        }
        Map<Integer, Double> res = new HashMap<Integer, Double>();
        for (Integer id : scores.keySet()) {
            Double sum = 0.0;
            while (!scores.get(id).isEmpty()) sum += scores.get(id).poll();
            res.put(id, sum/5);
        }
        return res;

    }
    public static void main(String[] args) {
        Result r1 = new Result(1, 95);
        Result r2 = new Result(1, 95);
        Result r3 = new Result(1, 91);
        Result r4 = new Result(1, 91);
        Result r5 = new Result(1, 93);
        Result r6 = new Result(1, 105);
 
        Result r7 = new Result(2, 6);
        Result r8 = new Result(2, 6);
        Result r9 = new Result(2, 7);
        Result r10 = new Result(2, 6);
        Result r11 = new Result(2, 6);
        Result[] arr = {r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11};
        Map<Integer, Double> res = getHighFive(arr);
 
        System.out.println(res.get(1) + " " +res.get(2));
    }
}