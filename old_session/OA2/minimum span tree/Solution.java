/*
Minimum Span Tree
*/
import java.util.*;
public class Solution {
    static class CntComparatorByCost implements Comparator<Connection>
    {
        @Override
        public int compare(Connection a, Connection b)
        {
            return a.cost - b.cost;
        }
    }
    static class CntComparatorByLetter implements Comparator<Connection>
    {
        @Override
        public int compare(Connection a, Connection b)
        {
            if (a.node1.equals(b.node1)) return a.node2.compareTo(b.node2);
            else return a.node1.compareTo(b.node1);
        }
    }
    public static List<Connection> getMST(List<Connection> connections) {
        Comparator<Connection> compareByCost = new CntComparatorByCost();
        Comparator<Connection> compareByLetter = new CntComparatorByLetter();
        
        Map<String, String> unions = new HashMap<>();   // k: node, v: root
        int counter = 0;                                // number of nodes
        for (Connection edge: connections)
        {
            if (!unions.containsKey(edge.node1)) {
                unions.put(edge.node1, edge.node1);
                counter++;
            }
            if (!unions.containsKey(edge.node2)) {
                unions.put(edge.node2, edge.node2);
                counter++;
            }
        }

        Collections.sort(connections, compareByCost);   // sort by cost
        List<Connection> res = new ArrayList<>();
        String rt1, rt2;
        for (Connection edge: connections) {
            rt1 = unions.get(edge.node1);
            rt2 = unions.get(edge.node2);
            while (rt1 != unions.get(rt1)) rt1 = unions.get(rt1);
            while (rt2 != unions.get(rt2)) rt2 = unions.get(rt2);
            if (rt1 != rt2)                             // not connected
            {
                unions.put(rt2, rt1);                   // connect them..
                res.add(edge);
                counter--;
            }
            if (counter == 1)                           // ... until now
            {
                Collections.sort(res, compareByLetter); // sort by letter
                break;
            }
        }
        return (counter == 1) ? res : new ArrayList<Connection>();
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        ArrayList<Connection> connections = new ArrayList<>();
//      connections.add(new Connection("Acity","Bcity",1));
//      connections.add(new Connection("Acity","Ccity",2));
//      connections.add(new Connection("Bcity","Ccity",3));
        connections.add(new Connection("A", "B", 6));
        connections.add(new Connection("B", "C", 4));
        connections.add(new Connection("C", "D", 5));
        connections.add(new Connection("D", "E", 8));
        connections.add(new Connection("E", "F", 1));
        connections.add(new Connection("B", "F", 10));
        connections.add(new Connection("E", "C", 9));
        connections.add(new Connection("F", "C", 7));
        connections.add(new Connection("B", "E", 3));
        connections.add(new Connection("A", "F", 1));

        List<Connection> res = getMST(connections);
        System.out.println("My code:");
        for (Connection c : res) {
            System.out.println(c.node1 + " -> " + c.node2 + " cost : " + c.cost);
        }
    }
 
}