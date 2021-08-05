#include <iostream>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
  int cnt = 0;
  int goodNodes(TreeNode* root) {
    dfs(root, INT_MIN);
    return cnt;
  }
  void dfs(TreeNode* node, int maxValInPath) {
    if (node == nullptr) return;
    if (node->val >= maxValInPath) cnt++;
    if (node->left != nullptr) dfs(node->left, max(maxValInPath, node->val));
    if (node->right != nullptr) dfs(node->right, max(maxValInPath, node->val));
    return;
  }
};