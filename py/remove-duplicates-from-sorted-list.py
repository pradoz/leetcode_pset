# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# linear time (worst case is when the is last two elements are the duplicates
# constant space for two ListNodes and integer counter
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        temp = None

        while curr != None and curr.next != None:
            if curr.val != curr.next.val:
                curr = curr.next
            else:
                # hold the next duplicate value in a temp node
                temp = curr.next

                # move the current next pointer to skip ahead one
                curr.next = curr.next.next
                del temp # delete temp node

        return head