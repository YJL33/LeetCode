/*
138. Copy List with Random Pointer

    Total Accepted: 76899
    Total Submissions: 293335
    Difficulty: Hard

A linked list is given such that each node contains an additional random pointer,
which could point to any node in the list or null.

Return a deep copy of the list.
*/
import java.util.*;
public class Solution {
    public static RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return head;

        // original: A->B->C->D
        // 1. copy:     A->A'->B->B'->C->C'->D->D'
        // 2. random:   A'.random = A.random.next
        // 3. extract copy

        RandomListNode dmy = new RandomListNode(0);
        RandomListNode copy, nexthead;
        dmy.next = head;

        while (head != null)
        {
            nexthead = head.next;
            copy = new RandomListNode(head.label);
            head.next = copy;
            copy.next = nexthead;
            head = nexthead;
        }

        head = dmy.next;
        while (head != null)
        {
            head.next.random = head.random.next;
            head = head.next.next;
        }

        RandomListNode dmy2 = new RandomListNode(0), cpy = dmy2, cur = dmy.next, nextcur;

        while (cur != null)
        {
            nextcur = cur.next.next;
            cpy.next = cur.next;
            cpy = cur.next;
            cur.next = nextcur;
            cur = nextcur;
        }
        return dmy2.next;
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        RandomListNode a = new RandomListNode(1);
        RandomListNode b = new RandomListNode(2);
        RandomListNode c = new RandomListNode(3);
        RandomListNode d = new RandomListNode(4);
        a.next = b;
        b.next = c;
        c.next = d;
        a.random = c;
        b.random = c;
        c.random = c;
        d.random = a;
        RandomListNode cur = a, cpy = copyRandomList(a);
        while (cur != null)
        {
            System.out.println(cur.random.label);
            System.out.println(cpy.random.label);
            cur = cur.next;
            cpy = cpy.next;
        }
        
    }
}