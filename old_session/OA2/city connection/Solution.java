/*
City Connection
*/
import java.util.*;

class Connection {
    public int cost;
    public String city1;
    public String city2;
    public Connection(String city1, String city2, Integer cost) {
        this.city1 = city1;
        this.city2 = city2;
        this.cost = cost;
    }
}
public class Solution {
    public static ArrayList<Connection> getLowCost(ArrayList<Connection> connections) {
        // if no connections => return null
        // for all cities (say n), and all connections (or edges, say m)
        // 1. sort all connections based on the cost
        // 2. pick up new edge based on cost, and update the map of existing cities
        // 3. repeat until all cities are connected.
        Collections.sort(connections, new Comparator<Connection>() {    // sort all connections
            @Override
            public int compare(Connection c1, Connection c2) {
                return c1.cost - c2.cost;
            }
        });
        Map citymap = new HashMap<String, String>();
        for (Connection c: connections) {
            if (!citymap.containsKey(c.city1)) {            // each city's is connected to itself
                citymap.put(c.city1, c.city1);
            }
            if (!citymap.containsKey(c.city2)) {
                citymap.put(c.city2, c.city2);
            }
        }
        ArrayList<Connection> ans = new ArrayList<Connection>();
        for (Connection c: connections) {
            String root1 = getRoot(citymap, c.city1);
            String root2 = getRoot(citymap, c.city2);
            if (!root1.equals(root2)) {
                citymap.put(root1, root2);                  // change root1's root as root2
                ans.add(c);
            }
            if (citymap.size()-1 == ans.size()) {           // check if cities are connected
                break;
            }
        }
        if (citymap.size()-1 != ans.size()) {
            System.out.print("not right!\n");
            return null;    // n cities need only n-1 connections
        }
        Collections.sort(ans, new Comparator<Connection>() {        // output as required format
            @Override
            public int compare(Connection c1, Connection c2) {
                if (c1.city1.equals(c2.city1)) {
                    return c1.city2.compareTo(c2.city2);
                }
                return c1.city1.compareTo(c2.city1);
            }
        });
        return ans;

    }
    public static String getRoot(Map<String, String> mp, String city) {
        if (!city.equals(mp.get(city))) {
             return getRoot(mp, mp.get(city));
        }
        return city;
    }
    public static void main(String[] args) {
        Connection e1 = new Connection("Seattle", "Portland", 5);
        Connection e2 = new Connection("Portland", "Boston", 5);
        Connection e3 = new Connection("Boston", "Chicago", 5);
        Connection e4 = new Connection("Chicago", "Denver", 59);
        Connection e5 = new Connection("Denver", "New York", 5);
        Connection e6 = new Connection("New York","Detroit", 57);
        Connection e7 = new Connection("Detroit", "Los Angeles", 5);
        Connection e8 = new Connection("Seattle", "Toronto", 5);
        Connection e9 = new Connection("Toronto", "Vancouver", 5);
        Connection e10 = new Connection("Los Angeles", "San Diego", 5);
        Connection e11 = new Connection("Chicago", "Denver", 5);
        Connection e12 = new Connection("Denver", "New York", 45);
        Connection e13 = new Connection("New York", "Detroit", 5);
        Connection e14 = new Connection("Detroit", "Los Angeles", 66);
        Connection e15 = new Connection("Detroit", "Toronto", 100);

        ArrayList cns = new ArrayList<Connection>();
        cns.add(e1);
        cns.add(e2);
        cns.add(e3);
        cns.add(e4);
        cns.add(e5);
        cns.add(e6);
        cns.add(e7);
        cns.add(e8);
        cns.add(e9);
        cns.add(e10);
        cns.add(e11);
        cns.add(e12);
        cns.add(e13);
        cns.add(e14);
        cns.add(e15);
        ArrayList<Connection> ans = getLowCost(cns);
        for (Connection c : ans) {
            System.out.print(c.city1);
            System.out.print(" ");
            System.out.print(c.city2);
            System.out.print(" ");
            System.out.println(c.cost);
        }
    }
}
