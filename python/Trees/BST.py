#creation pf binary search tree and iterations
#creation of node
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insertion(self,data):
        if self.data<data:
            if self.right is None:
                self.right=node(data)
            else:
                self.right.insertion(data)
        else:
            if self.left is None:
                self.left=node(data)
            else:
                self.left.insertion(data)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)  
            print(root.data,end=" ")
root=node(100)
root.insertion(60)
root.insertion(200)
root.insertion(56)
root.insertion(280)
root.insertion(300)
root.insertion(60)
root.insertion(80)
print("inorder: ")
root.inorder(root) 
print()
print("preorder: ")
root.preorder(root)
print()
print("postorder: ")
root.postorder(root)
