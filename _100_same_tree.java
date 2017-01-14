"""
100. Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are equal if they are structurally identical and the nodes have the same value.
"""
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p != null && q != null) {
            return (p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right));
        }
        else return (p == null && q == null);
    }
}