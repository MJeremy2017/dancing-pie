from queue import PriorityQueue
import time


class Node:
    def __init__(self, key, value, expiration_time):
        self.key = key
        self.value = value
        self.expiration_time = expiration_time

    def __lt__(self, other):
        return self.expiration_time < other.expiration_time


class ExpireMap:
    def __init__(self):
        self.mp = {}
        self.q = PriorityQueue()

    def insert(self, key, value, duration):
        expiration_time = self.get_now() + duration
        node = Node(key, value, expiration_time)
        self.q.put(node)
        self.mp[key] = node

    def get_value(self, key):
        self.clean_expired()
        return self.mp.get(key)

    @staticmethod
    def get_now():
        return int(time.time())

    def clean_expired(self):
        now = self.get_now()
        while not self.q.empty():
            if self.q.queue[0] < now:
                self.q.get()
            else:
                break