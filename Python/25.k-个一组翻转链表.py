#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        hair = ListNode(0)
        prev = hair
        hair.next = head

        while head:
            tail = prev

            for i in range(k):
                tail = tail.next

                if not tail:
                    return hair.next
                
            next = tail.next
            head, tail = self.reverse(head, tail)

            prev.next = head
            tail.next = next
            prev = tail
            head = tail.next
        
        return hair.next
    
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head

        while(prev != tail):
            next = p.next
            p.next = prev
            prev = p
            p = next

        return tail, head

        
# @lc code=end

