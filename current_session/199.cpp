 
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

//  Definition for a binary tree node.
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
    vector<int> rightSideView(TreeNode* root) {
        // check layer by layer
        // use stack
        // queue<TreeNode*>mQ;
        vector<TreeNode*> layer;
        layer.push_back(root);
        vector<int> res;
        while (layer.size() > 0) {
            TreeNode nd = *layer.at(layer.size()-1);
            res.push_back(nd.val);
            vector<TreeNode*> nextLayer;
            for (int i = 0; i < layer.size(); i++) {
                TreeNode x = *layer.at(i);
                if (x.left) nextLayer.push_back(x.left);
                if (x.right) nextLayer.push_back(x.right);
            }
            layer = nextLayer;
        }
        return res;
    }
};
