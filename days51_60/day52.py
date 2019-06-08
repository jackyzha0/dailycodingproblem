'''
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''
from collections import OrderedDict

class LRU:
    def __init__(self, cache_size):
        self.n = cache_size
        self.data = OrderedDict()

    def get(self, key):
        if key in self.data.keys:
            val = self.data.pop(key)
            self.data[key] = val
            return val
        else:
            return None

    def set(self, key, value):
        if key in self.data.keys:
            self.data.pop(key)
        else:
            if len(self.data) >= self.n:
                self.data.popitem(last=False) #FIFO Order

        self.data[key] = value
