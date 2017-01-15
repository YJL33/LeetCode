/*
Order dependency 
*/
import java.util.*;
public class Solution {

    static Map<String, ArrayList<String>> reqmap = new HashMap<>();
    static Map<String, Integer> visit = new HashMap<>();
    static List<Order> res = new ArrayList<>();

    public static Boolean dfs(List<Order> result, String x)
    {
        if (visit.get(x) == -1) return false;
        if (visit.get(x) == 1) return true;
        visit.put(x, 1);                    // mark it as 1
        for (String y: reqmap.get(x)) {
            if (dfs(res, y)) return true;   // if meet 1 again means there's a loop
        }
        visit.put(x, -1);                   // check PASSED, remark all of them as -1
        res.add(new Order(x));
        return false;
    }

    public static List<Order> findOrder(List<OrderDependency> dependency)
    {       
        // summarize pre-requisites (dependents) for each order.
        for (OrderDependency i: dependency)
        {
            if (!reqmap.containsKey(i.order.orderName)) {
                reqmap.put(i.order.orderName, new ArrayList<String>());
            }
            if (!reqmap.containsKey(i.dependent.orderName)) {
                reqmap.put(i.dependent.orderName, new ArrayList<String>());
            }
            if (!visit.containsKey(i.order.orderName)) {
                visit.put(i.order.orderName, 0);
            }
            if (!visit.containsKey(i.dependent.orderName)) {
                visit.put(i.dependent.orderName, 0);   
            }
            reqmap.get(i.order.orderName).add(i.dependent.orderName);
        }

        // put those don't need any pre-requisite into result first
        for (String n: reqmap.keySet()) {
            if (reqmap.get(n).size() == 0) {
                res.add(new Order(n));
                visit.put(n, -1);
            }
        }
        // dfs
        for (String n: reqmap.keySet()) {
            if (dfs(res, n)) return null;       // true => there's a loop
        }

        return res;
    }

    public static List<Order> findOrder2(List<OrderDependency> dependency)
    {
        Map<String, Integer> inmap = new HashMap<>();
        Map<String, List<String>> outmap = new HashMap<>();
        for (OrderDependency i: dependency)
        {
            if (!inmap.containsKey(i.dependent.orderName)) {
                inmap.put(i.dependent.orderName, 0);
            }
            if (!inmap.containsKey(i.order.orderName)) {
                inmap.put(i.order.orderName, 0);
            }
            inmap.put(i.order.orderName, inmap.get(i.order.orderName) + 1);
            if (!outmap.containsKey(i.dependent.orderName)) {
                outmap.put(i.dependent.orderName, new ArrayList<String>());
            }
            outmap.get(i.dependent.orderName).add(i.order.orderName);
        }
        List<Order> res = new ArrayList<>();
        Queue<String> queue = new LinkedList<>();
        for (String i: inmap.keySet())
        {
            if (inmap.get(i) == 0) queue.offer(i);
        }
        while (!queue.isEmpty())
        {
            String s = queue.poll();
            res.add(new Order(s));
            if (outmap.containsKey(s))
            {
                for (String o: outmap.get(s))
                {
                    inmap.put(o, inmap.get(o) - 1);
                    if (inmap.get(o) == 0) queue.offer(o);
                }
            }
            outmap.remove(s);
        }
        return res;
    }
    public static void main(String[] args)
    {
        System.out.println("Ans should be: C E A D B");
        List<OrderDependency> input = new ArrayList<>();
        input.add(new OrderDependency(new Order("A"), new Order("E")));
        input.add(new OrderDependency(new Order("D"), new Order("E")));
        input.add(new OrderDependency(new Order("A"), new Order("C")));
        input.add(new OrderDependency(new Order("B"), new Order("D")));
        
        List<Order> output = findOrder(input);
        System.out.print("my code: ");
        for (Order i: output) System.out.print(i.orderName + " ");
        System.out.print("\n");

        List<Order> output2 = findOrder2(input);
        System.out.print("4season's code: ");
        for (Order i: output2) System.out.print(i.orderName + " ");
        System.out.print("\n");
    }
}