# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time: O(max(m, n)), where m and n are the length of the two lists.
    # Space: O(max(m, n) + 1) => O(max(m, n)) to construct the new list
    def addTwoNumbersIteratively(self, l1, l2: ListNode) -> ListNode:
        a = l1
        b = l2
        carry = 0
        digit = curr = None

        while a or b:
            val = a.val + b.val + carry
            carry = val // 10
            if not curr:
                digit = curr = ListNode(val % 10)
            else:
                curr.next = ListNode(val % 10)
                curr = curr.next

            # if one list is longer, assign a zero to the other
            if a.next or b.next or carry > 0:
                if not a.next:
                    a.next = ListNode(0)
                if not b.next:
                    b.next = ListNode(0)
            elif carry > 0:
                digit.next = ListNode(carry)
            a = a.next
            b = b.next
        return digit

    # O(n) time and space. could get weird with recursive calls stored on the
    # stack. O(2n) still simplifies to O(n)
    def addTwoNumbersRecursively(self, l1, l2: ListNode, carry: int) -> ListNode:
        val = l1.val + l2. val + carry
        carry = val // 10
        digit = ListNode(val % 10) # modulo the radix
        if l1.next or l2.next:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            digit.next = self.addTwoNumbersRecursively(l1.next, l2.next, carry)
        elif carry > 0:
            digit.next = ListNode(carry)
        return digit




