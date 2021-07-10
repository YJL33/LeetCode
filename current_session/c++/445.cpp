#include <iostream>
#include <vector>

using namespace std;

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
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    // go through to the end of both linked list
    // use stack to store all values
    vector<int> stack1, stack2;
    while (l1) { stack1.push_back(l1->val); l1 = l1->next;}
    while (l2) { stack2.push_back(l2->val); l2 = l2->next;}
    int m = stack1.size(), n = stack2.size();
    int sum = 0, carry = 0;
    ListNode *head = nullptr, *newHead = nullptr;
    for (int i = m - 1, j = n - 1; i >= 0 || j >= 0 || carry > 0; i--, j--) {
      sum = carry;
      if (i>=0) sum += stack1[i];
      if (j>=0) sum += stack2[j];
      carry = sum/10;
      newHead = new ListNode(sum%10);
      newHead->next = head;
      head = newHead;
    }
    return head;
  }
};

// class Solution {
// public:
//   ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
//     // reverse both linkedList
//     ListNode* prev1=nullptr;
//     ListNode* prev2=nullptr;
//     while (l1) {
//       ListNode* next = l1->next;
//       l1->next = prev1;
//       prev1 = l1;
//       l1 = next;
//     }
//     while (l2) {
//       ListNode* next = l2->next;
//       l2->next = prev2;
//       prev2 = l2;
//       l2 = next;
//     }
//     // add 2 nums
//     l1=prev1;
//     l2=prev2;
//     ListNode* head = nullptr;
//     int sum=0, carry=0;
//     while (l1 != NULL || l2 != NULL) {
//       sum = carry;
//       // cout<<"sum"<<sum<<endl;
//       if (l1 != NULL) {sum += l1->val; l1 = l1->next;}
//       if (l2 != NULL) {sum += l2->val; l2 = l2->next;}
//       ListNode* n = new ListNode(sum%10, head);
//       head = n;
//       carry = sum/10;
//     }
//     if (carry!=0) {
//       ListNode* n = new ListNode(carry, head);
//       head = n;
//     }
//     return head;
//   }
// };