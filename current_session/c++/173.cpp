#include <iostream>
#include <vector>

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

class BSTIterator {
public:
  BSTIterator(TreeNode* root) {
    dfs(root);
  }

  int next() {
    return valueArray[cur++];
  }

  bool hasNext() {
    return cur<valueArray.size();
  }
private:
  int cur = 0;
  vector<int> valueArray;
  void dfs(TreeNode* node) {
    if (node == nullptr) return;
    if (node->left != nullptr) dfs(node->left);
    valueArray.push_back(node->val);
    if (node->right != nullptr) dfs(node->right);
    return;
  }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */