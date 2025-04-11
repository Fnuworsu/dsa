"""
Implementing queues using linkedlist
"""
class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
class Queue:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def __repr__(self):
        return f"{self.head}"
    
    def appendleft(self, val): 
        self.head = ListNode(val, self.head)
        self.size += 1
    
    def append(self, val):
        if not self.head:
            self.appendleft(val)
            return
        
        temp = self.head
        self.size += 1

        while temp.next:
            temp = temp.next
        
        temp.next = ListNode(val)
    
    def popleft(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1
    
    def pop(self):
        if not self.head:
            return
        temp = self.head
        self.size -= 1

        while temp.next.next:
            temp = temp.next
        
        temp.next = temp.next.next
    
q = Queue()
q.append(2)
q.append(3)
q.appendleft(4)
q.appendleft(5)

print(q)
print(len(q))

q.pop()
q.popleft()

print(q)
print(len(q))