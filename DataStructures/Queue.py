class Queue:
    def __init__(self, maxSize:int = 5):
        self.list = []
        self.maxSize = maxSize
        self.frontIndex = 0
        self.lastIndex = 0
    
    def enqueue(self, item):
        if self.isFull():
            print('Queue has reached max capacity.')
        else:
            self.list.append(item)
            self.frontIndex += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            self.lastIndex += 1
            return self.list[self.lastIndex - 1]
    
    def isEmpty(self) -> bool:
        if self.frontIndex == self.lastIndex:
            return True
        else:
            return False
    
    def isFull(self) -> bool:
        if self.frontIndex == self.maxSize:
            return True
        else:
            return False
