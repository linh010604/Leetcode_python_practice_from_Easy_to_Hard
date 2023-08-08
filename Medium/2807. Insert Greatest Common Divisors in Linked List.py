# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def gcd(a,b) :
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
    
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        crt = 0
        crt += head.val
        head = head.next
        dummy = res = ListNode(crt)
     
        while head:
            crt1 = head.val
            a = gcd(crt,crt1)
            crt = crt1
            res.next = ListNode(a)
            res = res.next
            res.next = ListNode(crt1)
            res = res.next
            head = head.next
        
        return dummy
        
