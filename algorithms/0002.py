class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        advance = False
        first = ListNode()
        result = None
        while l1 or l2:
            if not result:
                result = first
            else:
                next_result = ListNode()
                result.next = next_result
                result = next_result
            if l1 and l2:
                tmp = l1.val + l2.val
                if advance:
                    tmp += 1
                advance = tmp >= 10
                result.val = tmp % 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                tmp = l1.val
                if advance:
                    tmp += 1
                advance = tmp >= 10
                result.val = tmp % 10
                l1 = l1.next
            elif l2:
                tmp = l2.val
                if advance:
                    tmp += 1
                advance = tmp >= 10
                result.val = tmp % 10
                l2 = l2.next

        if advance:
            result.next = ListNode(1, None)

        return first
