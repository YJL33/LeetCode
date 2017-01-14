/*
K Closest Points
Problem:
Find the K closest points to the origin in 2D plane,
given an array containing N points.
You can assume K is much smaller than N and N is very large.
You need only use standard math operators
(addition, subtraction, multiplication, and division).
*/
import java.util.*;
public class Solution {
    private static double distance(Point a, Point b)
    {
        return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
    }
     
    public static Point[] closestPoint(Point[] points, final Point origin, int k)
    {
        if (points == null || points.length < k) return points;    // special case
        Arrays.sort(points, new Comparator<Point>() {              // sort the points
            @Override
            public int compare(Point a, Point b)
            {
                return Double.compare(distance(a, origin), distance(b, origin));
            }
        });
        Point[] res = new Point[k];
        for (int i = 0; i < k; i++) {                               // get the first k points
            res[i] = points[i];
        }
        return res;
    }
    public static Point[] closestPoint2(Point[] points, final Point origin, int k)
    {
        if (points == null || points.length < k) return points;    // special case
        // Use a priority queue (heap)
        PriorityQueue<Point> pq = new PriorityQueue<Point>(new Comparator<Point>()
        {
            @Override
            public int compare(Point a, Point b)
            {
                return Double.compare(distance(a, origin), distance(b, origin));
            }
        });
        for (Point p : points) {
            pq.add(p);
            if (pq.size() > k) pq.poll();
        }
        return pq.toArray(new Point[k]);
    }

    public static void main(String[] args)
    {
        Point origin = new Point(0, 0);
        Point[] input = new Point[]{new Point(0, 2), new Point(1, 1), new Point(-1, 0), new Point(2, 0), new Point(3, 0)};
        Point[] output = closestPoint2(input, origin, 4);
        System.out.println("input");
        for(Point i : input) System.out.print("("+i.x+", "+i.y+") ");
        System.out.println("");
        System.out.println("output");
        for(Point i : output) System.out.print("("+i.x+", "+i.y+") ");        
    }
}