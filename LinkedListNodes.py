#Linked ListNodes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


#Testing

node = ListNode(5)
print(node)  # Output: 5

#Interacting without de __str__ fixed return method:

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

current = node1
while current:
    print(current.val)
    current = current.next

# Output: 1 2 3 