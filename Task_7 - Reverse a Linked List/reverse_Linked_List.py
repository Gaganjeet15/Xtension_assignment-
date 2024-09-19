class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse current node's pointer
            prev = current            # Move pointers one position forward
            current = next_node
        self.head = prev
        
linked_list = SinglyLinkedList()

# Append values to the list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

# Print the original list
print("Original list:")
linked_list.print_list()

# Reverse the list
linked_list.reverse()

# Print the reversed list
print("Reversed list:")
linked_list.print_list()
