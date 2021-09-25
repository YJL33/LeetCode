#include <iostream>
#include <vector>

using namespace std;

// Definition for a Node.
class Node {
public:
  int val;
  Node* left;
  Node* right;
  Node* next;

  Node() : val(0), left(NULL), right(NULL), next(NULL) {}

  Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

  Node(int _val, Node* _left, Node* _right, Node* _next)
      : val(_val), left(_left), right(_right), next(_next) {}
};


class Solution {
public:
  Node* connect(Node* root) {
    if (root == nullptr) return root;
    vector<Node*> layer;
    layer.push_back(root);

    while (layer.size()!=0) {
      vector<Node*> nextLayer;
      Node* prev = nullptr;
      // handle current layer
      while (layer.size() != 0) {
        Node* nd = layer[layer.size()-1];
        nd -> next = prev;
        prev = nd;
        layer.pop_back();
        if (nd -> right != nullptr) nextLayer.push_back(nd->right);
        if (nd -> left != nullptr) nextLayer.push_back(nd->left);
      }
      // go to next layer
      reverse(nextLayer.begin(), nextLayer.end());
      layer = nextLayer;
    }

    return root;
  }
};

int main() {
  Node a = Node(1);
  Node b = Node(2);
  Node c = Node(3);
  Node d = Node(4);
  Node e = Node(5);
  Node f = Node(6);
  Node g = Node(7);
  a.left = &b;
  a.right = &c;
  b.left = &d;
  b.right = &e;
  c.left = &f;
  c.right = &g;
  // cout << Solution().connect(&a) << endl;
  // clang++ -std=c++17 c++/116.cpp -o 116 && ./116 -v
  auto node = Solution().connect(&a);
  vector<Node*> heads;
  while (node != nullptr) {
    heads.push_back(node);
    node = node->left;
  }
  for (auto x:heads) {
    Node* y = x;
    while (y != nullptr) {
      cout << y->val;
      y = y -> next;
    }
    cout << endl;
  }
}