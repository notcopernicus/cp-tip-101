class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_elements(head, val):
    curr = head
    total = 0
    while curr:
        if curr.value == val:
            total += 1
        curr = curr.next
    return total

# Build the list: 4 → 4 → 2 → 2
node1 = Node(4)
node2 = node1.next = Node(4)
node3 = node2.next = Node(2)
node4 = node3.next = Node(2)

# Example usage
print(count_elements(node1, 2))  # Output: 2
print(count_elements(node1, 4))  # Output: 2
print(count_elements(node1, 5))  # Output: 0
