from LinkedList import LinkedList
from LinkedListStack import LinkedListStack
from LinkedListQueue import LinkedListQueue

'''ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.prepend("X")
ll.prepend("Z")

ll.delete_from_head()
ll.delete_from_head()

ll.delete_from_tail()

ll.print_list()'''

# Test out stack
print("=" * 50)
print("TESTING LINKED LIST STACK")
print("=" * 50)

stack = LinkedListStack()

# Test adding elements to stack
print("\nAdding elements: 1, 2, 3, 4")
stack.enqueue(1)
stack.enqueue(2)
stack.enqueue(3)
stack.enqueue(4)

# Test viewing top element
print(f"Top element (front): {stack.front()}")  # Should be 4

# Test removing elements (LIFO order)
print("\nRemoving elements:")
print(f"Removed: {stack.dequeue()}")  # Should be 4
print(f"Removed: {stack.dequeue()}")  # Should be 3
print(f"Top element now: {stack.front()}")  # Should be 2

# Add more elements
print("\nAdding 5 and 6")
stack.enqueue(5)
stack.enqueue(6)
print(f"Top element: {stack.front()}")  # Should be 6

# Remove all remaining elements
print("\nRemoving all remaining elements:")
print(f"Removed: {stack.dequeue()}")  # 6
print(f"Removed: {stack.dequeue()}")  # 5
print(f"Removed: {stack.dequeue()}")  # 2
print(f"Removed: {stack.dequeue()}")  # 1

# Test empty stack
print("\nTesting empty stack:")
print(f"Dequeue from empty: {stack.dequeue()}")  # Should be None
print(f"Front of empty: {stack.front()}")  # Should be None

# Test out queue
print("\n" + "=" * 50)
print("TESTING LINKED LIST QUEUE")
print("=" * 50)

queue = LinkedListQueue()

# Test adding elements to queue
print("\nAdding elements: A, B, C, D")
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.enqueue("D")

# Test viewing front element
print(f"Front element: {queue.front()}")  # Should be A

# Test removing elements (FIFO order)
print("\nRemoving elements:")
print(f"Removed: {queue.dequeue()}")  # Should be A
print(f"Removed: {queue.dequeue()}")  # Should be B
print(f"Front element now: {queue.front()}")  # Should be C

# Add more elements
print("\nAdding E and F")
queue.enqueue("E")
queue.enqueue("F")
print(f"Front element: {queue.front()}")  # Should still be C

# Remove all remaining elements
print("\nRemoving all remaining elements:")
print(f"Removed: {queue.dequeue()}")  # C
print(f"Removed: {queue.dequeue()}")  # D
print(f"Removed: {queue.dequeue()}")  # E
print(f"Removed: {queue.dequeue()}")  # F

# Test empty queue
print("\nTesting empty queue:")
print(f"Dequeue from empty: {queue.dequeue()}")  # Should be None
print(f"Front of empty: {queue.front()}")  # Should be None

print("\n" + "=" * 50)
print("ALL TESTS COMPLETED!")
print("=" * 50)
