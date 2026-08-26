class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node from group_prev
            kth = self.getKth(group_prev, k)

            # Fewer than k nodes remain
            if not kth:
                break

            group_next = kth.next

            # Reverse current group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect reversed group
            old_group_start = group_prev.next
            group_prev.next = kth
            group_prev = old_group_start

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr