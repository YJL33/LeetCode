/*
206. Reverse Linked List

    Total Accepted: 151368
    Total Submissions: 358350
    Difficulty: Easy

Reverse a singly linked list.
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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) {
        	ListNode temp = head;
        	head = head.next;
        	temp.next = prev;
        	prev = temp;
        }
        return prev;
    }
}