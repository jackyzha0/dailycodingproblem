# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        href = r = ListNode(0)
        carry = 0
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            res = (v1 + v2 + carry) % 10
            r.next = ListNode(res)
            r = r.next
            carry = (v1 + v2 + carry)//10
            l1 = l1.next
            l2 = l2.next

        while l1:
            v1 = l1.val
            res = (v1 + carry) % 10
            r.next = ListNode(res)
            r = r.next
            carry = (v1 + carry)//10
            l1 = l1.next

        while l2:
            v2 = l2.val
            res = (v2 + carry) % 10
            r.next = ListNode(res)
            r = r.next
            carry = (v2 + carry)//10
            l2 = l2.next
        if carry == 1:
            r.next = ListNode(1)
        return href.next
