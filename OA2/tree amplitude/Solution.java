/*
Tree Amplitude

In a binary tree T, a path P is a non-empty sequence of nodes of tree such that,
each consecutive node in the sequence is a subtree of its preceding node.

In the example tree, the sequences [9, 8, 2] and [5, 8, 12] are two paths,
while [12, 8, 2] is not.

The amplitude of path P is the maximum difference among values of nodes on path P.
The amplitude of tree T is the maximum amplitude of all paths in T.
When the tree is empty, it contains no path, and its amplitude is treated as 0.

For exmaple.

Input:

         5
       /   \
     8       9
   /  \     /  \ 
  12   2   8   4
          /    /
        2    5

Output:
7
Explanation:
The paths [5, 8, 12] and [9, 8, 2] have the maximum amplitude 7.
*/
import java.util.*;
class TreeNode
{
    public TreeNode left, right;
    public int  val;
    public TreeNode(String val)
    {
        this.val = Integer.parseInt(val);
    }
}
public class Solution {
 
    public static TreeNode buildTree(String[] input)
    {
        int index = 0;
        TreeNode root = new TreeNode(input[index++]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while(index < input.length)
        {
             
            int size = queue.size();
            for(int i = 0; i< size; i++)
            {
                TreeNode t = queue.poll();
                if(index >= input.length) return root;
                if(!input[index].equals("*"))
                {
                    t.left = new TreeNode(input[index]);
                    queue.offer(t.left);
                }
                index++;
                if(index >= input.length) return root;
                if(!input[index].equals("*"))
                {
                    t.right = new TreeNode(input[index]);
                    queue.offer(t.right);
                }
                index++;
                if(index >= input.length) return root;
            }
        }
        return root;
    }
     
    public static int amplitude(TreeNode root)
    {
        if (root == null) return 0;
        return helper(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    public static int helper(TreeNode node, int big, int small)
    {
        if (node == null) return big-small;
        if (node.val > big) big = node.val;
        if (node.val < small) small = node.val;
        return Math.max(helper(node.left, big, small), helper(node.right, big, small));
    }
 
    public static void main(String[] args)
    {
        String[] input = {"5", "-8", "9", "-12", "2", "8", "4", "*", "*", "*", "*", "2", "*", "5"};
        TreeNode root = buildTree(input);
        System.out.println(amplitude(root));
    }
}