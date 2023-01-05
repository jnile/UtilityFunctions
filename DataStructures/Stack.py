class Stack:
    def __init__(self, maxSize:int = 5):
        self.list = []
        self.maxSize = maxSize

    def __str__(self) -> str:
        output = "{"

        for item in self.list:
            output += f"{item}, "

        if(len(output) > 1):
            output = output[:len(output)-2]
        
        output += '}'

        return output
    
    def push(self,item):
        if(self.isFull()):
            print("Stack is full")
        else:
            self.list.append(item)
    
    def pop(self):
        if(self.isEmpty):
            print("Stack is empty!")
            return None
        else:
            return self.list.pop()
    
    def isEmpty(self) -> bool:
        if len(self.list) == 0 :
            return True
        else:
            return False
    
    def isFull(self) -> bool:
        if(len(self.list) == self.maxSize):
            return True
        else:
            return False
    
    def top(self):
        return self.list(len(self.list)-1)