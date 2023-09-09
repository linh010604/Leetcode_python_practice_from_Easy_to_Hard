# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        d = list()

        while head :
            d.append(head.val)
            head = head.next

        res = nums = ListNode(0)

        for i in range(left-1) :
            nums.next = ListNode(d[i])
            nums = nums.next

        for i in range(right - 1,left-2,-1) :
            nums.next = ListNode(d[i])
            nums = nums.next

        for i in range(right,len(d)) :
            nums.next = ListNode(d[i])
            nums = nums.next

        return res.next
