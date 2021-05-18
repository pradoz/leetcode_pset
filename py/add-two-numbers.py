# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        carry = 0

        while l1 or l2 or carry:
            val1 = 0
            val2 = 0
            if l1:
                val1 += l1.val
                l1 = l1.next
            if l2:
                val2 += l2.val
                l2 = l2.next

            num = val1 + val2 + carry
            carry = num // 10
            digit = num % 10

            curr.next = ListNode(digit)
            curr = curr.next

        return head.next









