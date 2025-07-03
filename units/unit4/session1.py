# write a function that takes n and returns true if it a prime num and false otherwise
# a prime num is a num greater than 1 that has no positive divisors other than 1 and its self



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# two pointer reverse a linked list
def reverse_list (self, head):
    # create initial previous and current nodes
    prev, curr = None, head
    # while the list is not empty, iterate
    while curr:
        tmp = curr.next # temp num to hold the next value
        curr.next = prev # reverse the link
        prev = curr # set the previous num to the current num and move on
        curr = tmp # set the current num to the temp
    # finally after iterating return the head
    return prev

 # --- Helpers for building & printing a list ---

def build_list(values):
    """Create a linked list from the given iterable of values and return its head."""
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

def print_list(head):
    """Prints the linked list in a -> b -> c format."""
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

# --- Test it! ---

# 1) Build a list 1 -> 2 -> 3 -> 4 -> 5
head = build_list([1, 2, 3, 4, 5])
print("Original:")
print_list(head)

# 2) Reverse it
# Note: reverse_list is defined to take a 'self' argument,
# so we can just pass None here if we're calling it as a standalone function.
reversed_head = reverse_list(None, head)

# 3) Print the reversed list
print("\nReversed:")
print_list(reversed_head)