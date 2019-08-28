/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line

        if(l1 == nullptr and l2 == nullptr) // Both lists are empty
            return nullptr;

        if(l1 == nullptr) // l1 is empty
            return l2;

        if(l2 == nullptr) // l2 is empty
            return l1;

        ListNode* head; // Create node to hold the head
        if (l1->val < l2->val) { // l1 < l2
            head = l1; // hold l1 in head
            l1 = l1->next; // move to next node in l1
        } else { // l1 >= l2
            head = l2; // hold l2 in head
            l2 = l2->next; // move to next node in l2
        }

        // helper function
        helper(l1, l2, head);
        return head;
    }
// private:
    void helper(ListNode* l1, ListNode* l2, ListNode* curr) {
        if (l1 != nullptr and l2 != nullptr) {
            if (l1->val < l2->val) {
                curr->next = l1; 
                curr = curr->next;
                l1 = l1->next;
                helper(l1, l2, curr);
            } else {
                curr->next = l2;
                curr = curr->next;
                l2 = l2->next;
                helper(l1, l2, curr);
            }
        } else if (l1 != nullptr) {
            curr->next = l1;
            curr = curr->next;
            l1 = l1->next;
            helper(l1, l2, curr);
        } else if (l2 != nullptr) {
            curr->next = l2;
            curr = curr->next;
            l2 = l2->next;
            helper(l1, l2, curr);
        }
    }
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ios_base::sync_with_stdio(false); cin.tie(nullptr); // random performance line
        if(l1 == nullptr) return l2;
        if(l2 == nullptr) return l1;

            ListNode *head = nullptr;
            if (l1->val > l2->val) {
                head = l2;
                l2 = l2->next;
            } else {
                head = l1;
                l1 = l1->next;
            }
            
            head->next = mergeTwoLists(l1, l2);
            return head;
    }
};