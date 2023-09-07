/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// Approach:
// Step 1: Split the Linked List into three segments, one before the reversed portion, one after the reversed portion, and the first and last node of the reversed portion. 
// Step 2: Reverse the portion that should be reversed. Don't forget to make endNode->next nullptr
// Step 3: Piece the three segments back together, keeping in mind that now end stores the start of the reversed portion and vice versa

class Solution {
public:

    // Reverses a linked list. Uses curr as the pointer to the current node and prev as the pointer to the next node
    void reverse(ListNode* currNode, ListNode* prevNode) {
        if (!currNode) {
            return;
        }

        reverse(currNode->next, currNode);
        currNode->next = prevNode;
    }

    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (left == right) return head; // Edge Case
        ListNode* start;
        ListNode* end;
        ListNode* currNode = head;

        ListNode* nodeBeforeReversedPortion = nullptr; // Stores the node right before the reversed portion of the list

        // Step 1
        int i;
        for (int i = 1; i <= right; i++) {
            if (i == left) start = currNode;
            else if (i == left - 1) nodeBeforeReversedPortion = currNode;
            else if (i == right) end = currNode;
            currNode = currNode->next;
        }

        ListNode* nodeAfterReversedPortion = currNode; // Stores the node right after the reversed portion of the list
        end->next = nullptr;

        // Step 2
        reverse(start, nullptr);

        // Step 3
        // Now start and end are switched
        start->next = nodeAfterReversedPortion;

        ListNode* c = head;

        if (left == 1) { // If the beginning of the ll is reversed
            return end;
        } else {
            nodeBeforeReversedPortion->next = end;
            return head;
        }
    }
};
