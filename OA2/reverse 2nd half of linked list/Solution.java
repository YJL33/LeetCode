/*
Reverse Second Half of Linked List
*/

public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        // record head, and find the half point
        ListNode slow = head, fast = head;
        while (fast.next != null && fast != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        // now, slow is the mid-point
        // from now on, every new point should be linked as tail.
        ListNode last = null, cur;
        while (slow.next != null)
        {
            cur = slow.next.next;
            slow.next.next = last;
            last = slow.next;
            slow.next = cur;
        }
        // now connect two part
        slow.next = last;
        return head;
    }
}