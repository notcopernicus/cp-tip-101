# Problem 1 take a list of strings and return the sum of these strings as an int
def sum_of_str (nums):
    sumo = 0
    for num in nums:
        sumo += int(num)
    return sumo
    # # return sum(int(nums) for num in nums)
    # return (sum(map(int, nums)))

print (sum_of_str(['111', '223', '332']))

# problem 2 remove duplicates of numbers

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(remove_duplicates([1, 2, 2, 2, 3, 4, 5]))



# problem 3 reverse a chars in a string s, but keep all non letter chars in place

def reverse(s):
    # extract letters andsd reverse them
    letters = [c for c in s if c.isalpha()][::-1]
    
    result = []
    # traverse s and find all non letter chars
    for char in s:
        if char.isalpha():
            result.append(letters.pop(0)) # reversed letter
        else:
            result.append(char) # non letter char 
    return ''.join(result)

print(reverse('a-bC-dEf-ghIj'))










class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# building the linked list
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

curr = node1
while curr:
    print(curr.val, end = ' -> ')
    curr = curr.next
print('None')

def reverseList (head: ListNode) -> ListNode:

    # create the current and previous nodes
    curr, prev = head, None

    # iterate over the LinkedList
    while curr:
        tmp = curr.next # we set a temporary variable equal to the currents' next node
        curr.next = prev # we reverse the link between the next node and the previous node
        prev = curr # we set the previous node to the current node
        curr = tmp # we set the current node to the temporary variable stored earlier
    return prev # after iterating, the previous node becomes the head (eg head = 1, 2 , 3 -> Null is now head = 3, 2, 1 -> Null)

reverseHead = reverseList(node1)


curr = reverseHead
while curr:
    print(curr.val, end=" → ")
    curr = curr.next
print("None")
