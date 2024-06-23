class Queue():
    def __init__(self, capacity, list_queue=[]):
        self.capacity = capacity
        self.list_queue = list_queue

    def enqueue(self, added_num):
        if len(self.list_queue) < self.capacity:
            self.list_queue.append(added_num)
        return f"Queue is full"

    def is_full(self):
        if len(self.list_queue) == self.capacity:
            return f"Queue is full"
        return f"Queue is not full"

    def first_element(self):
        if not self.list_queue:
            return f"Queue is empty"
        first_value = self.list_queue[0]
        return first_value

    def dequeue(self):
        if not self.list_queue:
            return f"Queue is empty"
        pop_value = self.list_queue.pop(0)
        return pop_value

    def is_empty(self):
        if not self.list_queue:
            return f"Queue is empty"
        return f"Queue is not empty"


queue_1 = Queue(capacity=5)
queue_1.enqueue(1)
queue_1.enqueue(2)
print(queue_1.is_full())
print(queue_1.first_element())
print(queue_1.dequeue())
print(queue_1.first_element())
print(queue_1.dequeue())
print(queue_1.is_empty())
