#include <iostream>
#include <vector>
#include <map>
#include <stack>

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
  vector<vector<int>> verticalTraversal(TreeNode* root) {
    // simply create a map and return sorted value
    helper(root, 0, 0);
    vector<vector<int>> res;
    for (int i=minPos; i<=maxPos; ++i) {
      vector<int> tmp;          // create tmp vector to store all nodes in pos i
      for (auto k: nodeMap[i]) {
        sort(k.second.begin(), k.second.end());     // sort nodes in same (depth/pos)
        for (auto x: k.second) {          // add nodes in different depth
          tmp.push_back(x);
        }
      }
      res.push_back(tmp);
    }
    return res;
  }

private:
  map<int, map<int, vector<int>> > nodeMap;        // key: pos, value: map- k:depth value:node values
  int minPos=0, maxPos=0;
  void helper(TreeNode* node, int depth, int pos) {
    // create a stack for each layer
    minPos = min(minPos, pos);
    maxPos = max(maxPos, pos);
    // nodeMap[pos].push_back(node->val);
    nodeMap[pos][depth].push_back(node->val);
    stack<TreeNode*> st;
    if (node->left != nullptr) helper(node->left, depth+1, pos-1);
    if (node->right != nullptr) helper(node->right, depth+1, pos+1);
    return;
  }
};