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
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry=0, sum=0;
        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;
        while (l1 != null || l2 != null) {
            int x = (l1 == null) ? 0 : l1.val;     // java supports oneline if
            int y = (l2 == null) ? 0 : l2.val;
            sum = x + y + carry;
            carry = sum/10;
            ListNode nd = new ListNode(sum%10);
            cur.next = nd;
            cur = cur.next;
            l1 = (l1 == null) ? null : l1.next;
            l2 = (l2 == null) ? null : l2.next;
        }
        if (carry != 0) {
            ListNode tail = new ListNode(carry);
            cur.next = tail;
        }
        return dummy.next;
    }
}