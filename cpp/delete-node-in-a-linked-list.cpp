/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode* next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// Note: we are assuming this never deletes the tail
class Solution {
public:
    // O(1)
    void deleteNode(ListNode* node) {
        // move the next value one node down
        node->val = node->next->val;

        ListNode* curr = node->next;

        // move the node's next pointer down one node
        node->next = node->next->next;

        delete curr;
        curr = nullptr;
    }
};