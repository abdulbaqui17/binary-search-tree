class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    
class bst:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    
    def rinsert(self,root,data):
        if root is None:
            return node(data)
        
        elif data<root.data:
            root.left=self.rinsert(root.left,data)
        
        else:
            root.right=self.rinsert(root.right,data)
        
        return root
    
    def search(self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if root.data == data or root is None:
            return root
        
        elif data<root.data:
            return self.rsearch(root.left,data)
        
        else:
            return self.rsearch(root.right,data)
    
    def inorder(self):
        l=[]
        self.rinorder(self.root,l)
        return l
    
    def rinorder(self,root,l):
        if root:
            self.rinorder(root.left,l)
            l.append(root.data)
            self.rinorder(root.right,l)
        
    def preorder(self):
        l=[]
        self.rpreorder(self.root,l)
        return l
    
    def rpreorder(self,root,l):
        if root:
            l.append(root.data)
            self.rpreorder(root.left,l)
            self.rpreorder(root.right,l)
        
    def postorder(self):
        l=[]
        self.rpostorder(self.root,l)
        return l
    
    def rpostorder(self,root,l):
        if root:
            self.rpostorder(root.left,l)
            self.rpostorder(root.right,l)
            l.append(root.data)
        
    def min(self,root):
        current=root
        while current.left is not None:
            current=current.left
        return current.data
    
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
        
    def rdelete(self,root,data):
        if root is None:
            return root
        
        elif data<root.data:
            root.left=self.rdelete(root.left,data)
            
        elif data>root.data:
            root.right=self.rdelete(root.right,data)
        
        else:
            if root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
            
            root.data=self.min(root.right)
            root.right=self.rdelete(root.right,root.data)
        return root
            

t=bst()
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(20)
t.insert(50)
print("inorder:",t.inorder())
print("the value is deleted",t.delete(50))
print("found",t.search(15).data)
print("inorder:",t.inorder())
#print("preorder:",t.preorder())
#print("postorder:",t.postorder())