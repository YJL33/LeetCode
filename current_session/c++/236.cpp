
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// dfs?
// 
class Solution {
public:
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    return dfs(root, p, q);
  }
private:
  // TreeNode* lca;
  TreeNode* dfs(TreeNode* node, TreeNode* p, TreeNode* q) {
    if (node == nullptr || node == p || node == q) return node;
    TreeNode* left = dfs(node->left, p, q);
    TreeNode* right = dfs(node->right, p, q);
    if (left != nullptr && right != nullptr) {
      return node;
    } else if (left != nullptr) {
      return left;
    } else if (right != nullptr) {
      return right;
    } else {
      return nullptr;
    }
  }
};