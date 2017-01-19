/*
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dmy = new ListNode(0);
        ListNode cur = dmy;
        while (l1 != null && l2 != null)
        {
            if (l1.val <= l2.val) {
                cur.next = l1;
                l1 = l1.next;
            }
            else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
        cur.next = (l1 != null) ? l1 : l2;
        return dmy.next
    }
}