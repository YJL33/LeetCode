#include <iostream>
#include <limits>

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
  bool isValidBST(TreeNode* root) {
    long ub = numeric_limits<long>::max();
    long lb = -1*numeric_limits<long>::max();
    return dfs(root, ub, lb);
  }
private:
  bool dfs(TreeNode* node, long upperBound, long lowerBound) {
    if (node == nullptr) return true;
    if (lowerBound < node->val && node->val < upperBound) {
      return dfs(node->left, long(node->val), lowerBound) && dfs(node->right, upperBound, long(node->val));
    } else {
      return false;
    }
  }
};