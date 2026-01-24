/*
 * @lc app=leetcode.cn id=25 lang=java
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode hair = new ListNode(0), prev = hair, tail = hair;
        hair.next = head;

        while(head != null){
            for(int i = 0; i < k; i++){
                tail = tail.next;

                if(tail == null)
                    return hair.next;
            }

            ListNode next = tail.next;
            ListNode[] meta = reverse(head, tail);
            head = meta[0];
            tail = meta[1];
            prev.next = head;
            tail.next = next;

            prev = tail;
            head = next;
        }

        return hair.next;
    }

    public ListNode[] reverse(ListNode head, ListNode tail){
        ListNode prev = tail.next, p = head, next = head.next;

        while(prev != tail){
            next = p.next;

            p.next = prev;
            prev = p;
            p = next;
        }

        return new ListNode[]{tail,head};
    }
}
// @lc code=end

