#include <iostream>
#include <vector>
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



// the naive approach: iterate all nodes
// store the value layer by layer
// and reverse if needed
// beware of the order of putting children into stack/queue
class Solution {
public:
  vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    int layer = 0;
    stack<TreeNode*> oddSt;
    stack<TreeNode*> evenSt;
    evenSt.push(root);
    vector<vector<int>> res;
    if (root == nullptr) return res;
    while (!evenSt.empty() || !oddSt.empty()) {
      vector<int> tmp{};
      if (oddSt.empty()) {     // oddSt is not empty -> odd layer (including root), from left to right
        while (!evenSt.empty()) {
          tmp.push_back(evenSt.top()->val);
          if (evenSt.top()->left != nullptr) oddSt.push(evenSt.top()->left);
          if (evenSt.top()->right != nullptr) oddSt.push(evenSt.top()->right);
          evenSt.pop();
        }
      } else {      // stack is not empty -> even layer, from right to left
        while (!oddSt.empty()) {
          tmp.push_back(oddSt.top()->val);
          if (oddSt.top()->right != nullptr) evenSt.push(oddSt.top()->right);
          if (oddSt.top()->left != nullptr) evenSt.push(oddSt.top()->left);
          oddSt.pop();
        }
      }
      res.push_back(tmp);
    }
    return res;
  }
};