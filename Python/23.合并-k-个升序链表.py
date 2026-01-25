#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists: List[Optional[ListNode]], l, r) -> Optional[ListNode]:
        if l == r:
            return lists[l]

        if l > r:
            return None
        
        mid = (l + r) // 2

        return self.merge_two_list(self.merge(lists, l, mid), self.merge(lists, mid + 1, r))

    def merge_two_list(self, a: List[Optional[ListNode]], b: List[Optional[ListNode]]) -> Optional[ListNode]:
        if a == None or b == None:
            if a == None:
                return b
            else:
                return a
            
        hair = ListNode(0)
        a_ptr = a
        b_ptr = b
        tail = hair

        while a_ptr != None and b_ptr != None:
            if a_ptr.val < b_ptr.val:
                tail.next = a_ptr
                a_ptr = a_ptr.next
            else:
                tail.next = b_ptr
                b_ptr = b_ptr.next

            tail = tail.next

        if a_ptr == None:
            tail.next = b_ptr
        else:
            tail.next = a_ptr

        return hair.next

# @lc code=end

