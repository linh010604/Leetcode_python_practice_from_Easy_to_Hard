# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        res = ress = ListNode(0)
        num = nums = ListNode(0)
        while head :
            a = head.val
            if a >= x :
                res.next = ListNode(a)
                res = res.next
            else:
                num.next = ListNode(a)
                num = num.next

            head = head.next
        num.next = ress.next

        return nums.next
