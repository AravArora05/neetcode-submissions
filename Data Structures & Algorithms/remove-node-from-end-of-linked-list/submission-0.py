# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #given the head of linked list
        #given an integer n, remove the nth node from end of list + return head
        dummy =first=prev=ListNode(0, head)
        count=0
        while count<=n:
            dummy=dummy.next
            count+=1
        while dummy:
            dummy=dummy.next
            first=first.next
        print(first.next.val)
        print(first.next.next)
        first.next=first.next.next
        return prev.next
        
        