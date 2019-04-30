'''
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

class log:
    def __init__(self):
        self.log = []

    def record(self, order_id):
        self.log.append(order_id)

    def get_last(self, i):
        return self.log[-i]

if __name__ == "__main__":
    l = log()
    l.record("1")
    l.record("3")
    l.record("4")
    print(l.log)
    print(l.get_last(2))
