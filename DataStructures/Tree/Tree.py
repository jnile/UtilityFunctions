class Node:
    def __init__(self, data) -> None:
        self.leftNode = None
        self.rightNode = None
        self.data = data
    
    def setLeftChild(self, data):
        self.leftNode = Node(data)
    
    def setRightChild(self, data):
        self.rightNode = Node(data)

    def getPreorderTraversal(self, output:str) -> str:
        output += str(self.data) + " "

        if (self.leftNode):
            output = self.leftNode.getPreorderTraversal(output)

        if (self.rightNode):
            output = self.rightNode.getPreorderTraversal(output)

        return output
    
    def getPostorderTraversal(self, output:str) -> str:
        if (self.leftNode):
            output = self.leftNode.getPostorderTraversal(output)

        if (self.rightNode):
            output = self.rightNode.getPostorderTraversal(output)

        output += str(self.data) + " "
        return output
    
    def getInorderTraversal(self, output:str) -> str:
        if (self.leftNode):
            output = self.leftNode.getInorderTraversal(output)

        output += str(self.data) + " "

        if (self.rightNode):
            output = self.rightNode.getInorderTraversal(output)

        
        return output

class Tree:
    def __init__(self, rootData) -> None:
        self.rootNode = Node(rootData)
    
    def preorderTraversal(self) -> str:
        return self.rootNode.getPreorderTraversal("")
    
    def postorderTraversal(self) -> str:
        return self.rootNode.getPostorderTraversal("")

    def inorderTraversal(self) -> str:
        return self.rootNode.getInorderTraversal("")

if __name__ == "__main__":
    x = Tree(1)
    x.rootNode.setLeftChild(2)
    x.rootNode.setRightChild(3)
    x.rootNode.leftNode.setLeftChild(4)
    print("Preorder: " + x.preorderTraversal())
    print("Inorder: " + x.postorderTraversal())
    print("Postorder: " + x.inorderTraversal())
