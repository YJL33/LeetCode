#include <iostream>
#include <vector>

using namespace std;

// Follow up: Could you do it in O(n) time and O(1) space?
// find the middle point -> reverse the first (or second half) -> compare the LL

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  bool isPalindrome(ListNode* head) {
    ListNode* node = head;
    vector<int> seen;
    while (node != nullptr) {
      seen.push_back(node->val);
      node = node->next;
    }
    int l=0, r=seen.size()-1;
    while (l<r && seen[l] == seen[r]) {
      ++l;
      --r;
    }
    return (l>=r);
  }
};