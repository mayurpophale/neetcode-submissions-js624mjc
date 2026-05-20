# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            a = current.val
            b = current.next.val
            x,y = a,b
            while y!=0:
                x,y = y,y%x

            gcd_node = ListNode(x)

            gcd_node.next = current.next
            current.next = gcd_node

            current = gcd_node.next

        return head