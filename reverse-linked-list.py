# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Original Solution
def reverseList(head):
    """
    head: ListNode
    rVal: ListNode
    """

    curr = head
    prev = None
    
    # Set the next of curr to prev and shift everything over one
    while curr is not None:            
        # Need next to store the next Node since the next of curr gets
        # set to prev.
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    # prev holds the last Node, which is now the first
    head = prev
    
    return head

# Slightly Optimized Solution
def reverseList(head):
    """
    head: ListNode
    rVal: ListNode
    """

    if head is not None:
        # Use head as prev and simply return head
        current = head.next
        head.next = None
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = head
            head = current 
            current = next_node

    return head