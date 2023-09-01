# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        d = list()

        for item in lists:
            while item :
                d.append(item.val)
                item = item.next

        d.sort()
        nums = res = ListNode(0)

        for item in d :
            nums.next = ListNode(item)
            nums = nums.next
        return res.next
        
