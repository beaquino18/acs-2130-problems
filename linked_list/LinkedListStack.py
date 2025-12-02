from LinkedList import LinkedList

class LinkedListStack:
  """Implements a stack (LIFO) using a linked list"""

  def __init__(self):
    self.ll_stack = LinkedList()

  def enqueue(self, new_data):
    """Add element to top of stack - O(1) time complexity"""
    self.ll_stack.prepend(new_data)

  def dequeue(self):
    """Remove and return element from top of stack - O(1) time complexity"""
    if self.ll_stack.head == None:
      return None
    top_data = self.ll_stack.head.data
    self.ll_stack.delete_from_head()
    return top_data

  def front(self):
    """View top element without removing - O(1) time complexity"""
    if self.ll_stack.head == None:
      return None
    return self.ll_stack.head.data
