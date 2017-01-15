/*
Maximum Subtree of Average
*/
import java.util.ArrayList;
public class Solution {
    static class SumCount
    {
        int sum;
        int count;
        public SumCount(int sum, int count)
        {
            this.sum = sum;
            this.count = count;
        }
    }
    static Node ans;
    static Double max;
    public static Node finder(Node root) {
        ans = null;
        max = 0.0;
        DFS(root);
        return ans;
    }
    public static SumCount DFS(Node node) {
        if (node == null) return (new SumCount(0, 0));
        if (node.children == null || node.children.size() == 0) return (new SumCount(node.val, 1));
        int sum=node.val, count=1;
        for (Node n: node.children) {
            SumCount sc = DFS(n);
            sum += sc.sum;
            count += sc.count;
        }
        if (((sum +0.0)/ count) > max) {
            max = ((sum +0.0)/ count);
            ans = node;
        }
        return new SumCount(sum, count);
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        Node l21 = new Node(2);
        Node l22 = new Node(3);
        Node l23 = new Node(4);
        Node l31 = new Node(5);
        Node l32 = new Node(5);
        Node l33 = new Node(5);
        Node l34 = new Node(5);
        Node l35 = new Node(5);
        Node l36 = new Node(5);
 
        l21.children.add(l31);
        l21.children.add(l32);
 
        l22.children.add(l33);
        l22.children.add(l34);
 
        l23.children.add(l35);
        l23.children.add(l36);
 
        root.children.add(l21);
        root.children.add(l22);
        root.children.add(l23);
 
        Node res = finder(root);
        System.out.println(res.val + " " + max);
    }
}