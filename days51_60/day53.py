'''
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.
'''

class queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):
        if len(outbox) == 0:
            while self.inbox:
                i = self.inbox.pop()
                self.outbox.append(i)
        return self.outbox.pop()
