/*
Overlap Rectangle
Problem:
Check whether two rectangles overlaps.
The bottem-left and top-right Node has been given.
*/
import java.lang.IllegalArgumentException;
public class Solution {
    // say A & C is bottom-left, B & D is top-right
    public static boolean hasOverlap(Node a, Node b, Node c, Node d)
    {
        int x1 = a.x, x2 = b.x, x3 = c.x, x4 = d.x;
        int y1 = a.y, y2 = b.y, y3 = c.y, y4 = d.y;
        if (x2 <= x1 || y2 <= y1 || x4 <= x3 || y4 <= y3) throw new IllegalArgumentException();
        if (x3 >= x2 || x4 <= x1 || y3 >= y2 || y4 <= y1) return false;
        return true;
    }
    public static void main(String[] args)
    {
        Node a = new Node(0, 0), b = new Node(2, 2), c = new Node(1, 0), d = new Node(4, 4);
        System.out.println(hasOverlap(a, b, c, d));
    }
}