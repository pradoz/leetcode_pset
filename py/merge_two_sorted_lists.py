# merge_two_sorted_lists.py

# Recursive solution
class Solution():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2: # if one of the lists is empty
            return l1 or l2 # then return the list that isnt empty
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
# Iterative soltuions
# both solutions have O(n) runtime and O(1) space complexity
# we have to visit every, element, but we aren't storing anything

class Solution():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            p1, p2 = l1, l2
            head = p1 # track the head of list
                   
            while p1 and p2: # while both lists still have nodes
                if p1.val < p2.val: # p1 < p2
                    if not p1.next: # check if p1 has no more nodes
                        p1.next = p2 # no nodes left => next is p2
                        break
                    else: # if p1 has more nodes
                        p1 = p1.next # p1 is the next part of the list
                else: # p1 >= p2
                    tmp = ListNode(p1.val) # create temp node
                    tmp.next = p1.next # make temp hold p1, then pass p2 to p1
                    p1.val = p2.val # now p1 can hold the next value from p2
                    p1.next = tmp # 
                    if not p1.next:
                        p1.next = p2.next
                        break
                    p2 = p2.next      
            
            return head if head else p2

class Solution():
    def mergeTwoLists(self, l1, l2):
        dummy = curr = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next