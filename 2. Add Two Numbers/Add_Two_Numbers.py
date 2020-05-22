# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        l_next = l
        c = 0
        while l1 or l2 or c:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            c, num = divmod(num1 + num2 + c, 10)
            l_next.next = ListNode(num)
            l_next = l_next.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return l.next


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))
