# Write a Python class that represents a singly linked list and then write a function to reverse the list.


Explanation:
1. The class "ListNode" represents a single node in our linked list
   * self.value: This stores the actual data of the node.
   * self.next: This is a reference to the next node in the list.
2. SinglyLinkedList represents whole linked list
   * It starts with head which points to start node of list.
3. The "append" function adds a new node to the end of the list.
   * If the list is empty (no head), it creates a new node and sets it as the head.
   * If the list isn't empty, it traverses to the last node and adds the new node there.
4. The "print_list" function prints the list.
5. The "reverse" functions has is init with 3 nodes prev, current, and next_node.
   * For each node, we save its next connection, point it backward, then step forward.
   * at the end the prev pointer points to new head of the list. 