
#BFS using depth

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
    def depth(self,root):
        if root is None:
            return 0  
        else:
            l=self.depth(root.left)
            r=self.depth(root.right)
        return max(l,r)+1  
    def levelwise(self,root):
        d=self.depth(root)
        for i in range(1,d+1):
            self.printlevelwise(root,i)
    
    def printlevelwise(self,root,level):
        if root is None:
            return
        if level==1:
            print(root.data)
        elif level>1:
            self.printlevelwise(root.left,level-1)
            self.printlevelwise(root.right,level-1)
            
root=node(100)
root.insertion(60)
root.insertion(200)
root.insertion(56)
root.insertion(280)
root.insertion(300)
root.insertion(70)
root.insertion(80)   
root.levelwise(root)
