/*Copyright [2017] <YJLee>
2. Add Two Numbers

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dmy(0), *cur = &dmy;
        int carry = 0;
        while (carry || l1 || l2) {
            int sum = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            carry = sum/10;
            cur->next = new ListNode(sum%10);
            cur = cur->next;
            l1 = (l1 ? l1->next : l1);      // one line if
            l2 = (l2 ? l2->next : l2);
        }
        return dmy.next;          // return head address
    }
};
