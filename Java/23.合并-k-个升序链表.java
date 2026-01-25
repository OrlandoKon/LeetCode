/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并 K 个升序链表
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
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode hair = new ListNode(Integer.MAX_VALUE);

        for(ListNode head : lists){
            ListNode cur = hair;
            
            while(head != null){
                while(cur.next != null && head.val > cur.next.val)
                    cur = cur.next;
                    
                ListNode next = head.next;
                head.next = cur.next;
                cur.next = head;
                head = next;
            }
        }

        return hair.next;
    }
}
// @lc code=end

