from LinkedList import LinkedList

class LinkedListQueue:

  def __init__(self):
    self.ll_queue = LinkedList()

  def enqueue(self, new_data):
    """Add element to rear of queue - O(1) time complexity"""
    self.ll_queue.append(new_data)

  def dequeue(self):
    """Remove and return element from front of queue - O(1) time complexity"""
    if self.ll_queue.head == None:
      return None
    front_data = self.ll_queue.head.data
    self.ll_queue.delete_from_head()
    return front_data

  def front(self):
    """View front element without removing - O(1) time complexity"""
    if self.ll_queue.head == None:
      return None
    return self.ll_queue.head.data
