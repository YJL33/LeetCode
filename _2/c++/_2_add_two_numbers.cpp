"""
2. Add Two Numbers

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {       // return the address of head
        int carry=0, sum=0;
        ListNode *h = NULL, **cur = &h;     // h points at head, cur move through tail.
        while (l1 != NULL || l2 != NULL) {
            sum = getValAndMoveOn(l1)+getValAndMoveOn(l2)+carry;
            carry = sum/10;
            ListNode *nd = new ListNode(sum%10);
            *cur = nd;                      // last node point to address of new node
            cur = &(nd->next);              // move to next position.
        }
        if (carry != 0) {
            ListNode *nd = new ListNode(carry);
            *cur = nd;
        }
        return h;
    }

private:
    int getValAndMoveOn(ListNode* &nd) {    // use non-const reference to change argument
        int x = 0;                          // here nd is an alias of (node l)
        if (nd != NULL) {
            x = nd->val;
            nd = nd->next;
        }
        return x;
    }
};