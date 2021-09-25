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

// handle layer by layer, can use deque to optimize (save reverse time)
class Solution {
public:
  Node* connect(Node* root) {
    // edge case
    if (root == nullptr) return root;
    // first layer
    vector<Node*> layer;
    layer.push_back(root);

    // handle layer by layer
    while (layer.size() != 0) {
      vector<Node*> nextLayer;
      Node* prev = nullptr;
      while (layer.size() != 0) {
        Node* n = layer[layer.size()-1];
        n->next = prev;
        prev = n;
        layer.pop_back();
        // craft next layer
        if (n->right != nullptr) {nextLayer.push_back(n->right);}
        if (n->left != nullptr) {nextLayer.push_back(n->left);}
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
  c.right = &g;
  a.right = &c;
  a.left = &b;
  b.left = &d;
  b.right = &e;
  // cout << Solution().connect(&a) << endl;
  // clang++ -std=c++17 c++/117.cpp -o 117 && ./117 -v
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