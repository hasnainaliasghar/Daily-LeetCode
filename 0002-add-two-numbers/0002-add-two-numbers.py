# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1 is None:
            return 0

        val1 = 0
        i = 1
        while l1 is not None:
            val1 += l1.val * 10 ** i
            l1 = l1.next
            i += 1

        val2 = 0
        i = 1
        while l2 is not None:
            val2 += l2.val * 10**i
            l2 = l2.next
            i += 1

        val1 = val1 // 10
        val2 = val2 // 10
        sum = val1+val2

        dummy = ListNode()
        current = dummy

        for digit_char in str(sum)[::-1]:
            current.next = ListNode(int(digit_char))   # create a NEW node, attach it
            current = current.next                     # NOW walk forward to that new node

        return dummy.next 
        
        return l3

