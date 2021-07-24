#include <iostream>
#include <queue>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
// handle in a order of "left->node->right"
// use a stack (to store unhandled node)
// for each node, if exist a left: 
// 1. add itself into stack
// 2. move to it's left (node = node.left)
// ...
// pop the stack: topNode
// prev.next, topNode.prev, prev = topNode, prev, topNode
// node = node.right

class Solution {
public:
  Node* treeToDoublyList(Node* root) {
    if (root == nullptr) return root;
    helper(root);    
    Node* head = chain();
    return head;
  }
private:
  // Node dummyHead = Node(0);
  // Node* prev = &dummyHead;
  Node* head;
  Node* prev;
  queue<Node*> queue;

  // add all nodes into the queue in a left-node-right order
  void helper(Node* nd) {
    if (nd->left) helper(nd->left);
    queue.push(nd);
    if (nd->right) helper(nd->right);
  }

  // chain all nodes 
  Node* chain() {
    head = queue.front();
    prev = queue.back();
    while (!queue.empty()) {
      Node* x = queue.front();
      prev->right = x;
      x->left = prev;
      prev = x;
      queue.pop();
    }
    return head;
  }
};