class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next   # save next
            curr.next = prev        # reverse link
            prev = curr             # move prev
            curr = next_node        # move curr

        return prev
