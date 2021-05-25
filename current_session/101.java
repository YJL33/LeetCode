/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        return helper(root.left, root.right);
    }

    private boolean helper(TreeNode l, TreeNode r) {
        if (l == null && r != null) return false;
        if (r == null && l != null) return false;
        if (r == null && l == null) return true;
        if (r.val != l.val) return false;
        return helper(r.right, l.left) && helper(l.right, r.left);
    }
}