# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
# recursively
# runtime O(n) since we have to iterate through every node in the list
# space complexity is O(n) since we store n recursive calls on the stack
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case
        if head is None:
            return head

        prev = self.reverseList(head.next)
        head.next.next = head
        return head




# iteratively
# runtime O(n) since we have to iterate through every node in the list
# space complexity is O(1) since we only use two node pointers to while
#   traversing the list. The space that is used can always be calculated with
#   sizeof(Node) * 2, because we use two pointer nodes, temp and curr.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        curr = head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
