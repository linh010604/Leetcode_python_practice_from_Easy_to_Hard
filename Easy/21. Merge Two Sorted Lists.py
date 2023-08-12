# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        kq = res = ListNode(0)

        while list1 or list2 :
            try:
                n1 = list1.val
            except:
                n1 = 101
            try:
                n2 = list2.val
            except:
                n2 = 101
            if n1 < n2 :
                res.next = ListNode(n1)
                list1 = list1.next
            else:
                res.next = ListNode(n2)
                list2 = list2.next
            
            res = res.next

        return kq.next
