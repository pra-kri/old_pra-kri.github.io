# BinaryTree implementation
# with a function that can find the depth of a node within a tree.

# LESSON; When implementing recursion within a class method, make sure you refer to the function through the next object. 
# e.g. use self.parent.recursive_function(), instead of self.recursive_function().



class BTNode:
    def __init__(self, value_item, parent_item = None):
        self.value = value_item        
        self.parent = parent_item
        self.left = None
        self.right = None
        self.counter = 0
        
    def addLeft(self, child):
        self.left = child
        child.parent = self
        
    def addRight(self, child):
        self.right = child
        child.parent = self
        
    def cutLeft(self):
        self.left.parent = None        
        self.left = None
        
    def cutRight(self):
        self.right.parent = None
        self.right = None
        
    def is_root(self):
        if self.parent == None:
            return True
        else:
            return False
    
    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False
            
     
    def getDepth(self):
        if self.parent == None:
            return 0
        counter1 =  1 + self.parent.getDepth()
        return counter1


aa = BTNode(199)
#bb = BTNode(12, aa)
bb = BTNode(12)
aa.addLeft(bb)
# kind of annoying: have to create the node before I add it as the child...
# TODO: find a way to do it better...
print(aa)
print('---------------------')
print(aa.left.parent.value)
  
print(bb.parent.value)          
aa.cutLeft()
print(bb.parent)
            
            
            
aaa = BTNode(1)
bbb = BTNode(2)
ccc = BTNode(3)
ddd = BTNode(4)
eee = BTNode(5)


aaa.addLeft(bbb)
bbb.addLeft(ccc)
bbb.addRight(ddd)
aaa.addRight(eee)





print(aaa.getDepth()) # should output 0. root node

print(bbb.getDepth()) # should output 1

print(ccc.getDepth()) # should output 2

print(ddd.getDepth()) # should output 2

print(eee.getDepth()) # should output 1
