# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(1)
class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Given: The linked list will have at least two elements.
        # if node is None:
        #     return

        temp = node
        node.val = node.next.val
        node.next = node.next.next
        del temp
