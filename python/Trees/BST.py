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
    def search(self,root,value):
        if root is not None:
            if root.data==value:
                print(value,"element is found",end=" ")
            elif root.data<value:
                self.search(root.right,value)
            elif root.data>value:
                self.search(root.left,value)
        else:
            print("element is not there")
    
    def minValueNode(self,root):
        current=root
        while(current.left is not None):
            current=current.left
        return current
        
    def delete(self,key,root):
        if root is None:
            return root
        if key<root.data:
            root.left=self.delete(key,root.left)
        elif key>root.data:
            root.right=self.delete(key,root.right)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
                
            temp=self.minValueNode(root.right)
            
            root.data=temp.data
            
            root.right=self.delete(temp.data,root.right)
            
        return root    
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
root.insertion(70)
root.insertion(80)
print("inorder: ")
root.inorder(root) 
print()
print("preorder: ")
root.preorder(root)
print()
print("postorder: ")
root.postorder(root)
print()
root.search(root,80)
print()
root.search(root,1000)
root.delete(200,root)
root.inorder(root)
print()
root.delete(300,root)
root.inorder(root)
print()
root.delete(60,root)
root.inorder(root)
