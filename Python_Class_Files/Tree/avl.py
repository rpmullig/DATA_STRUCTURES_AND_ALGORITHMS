# AVL Trees, by Elizabeth Feicke


class AVLNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None



def less_than(x,y):
    return x < y

class AVLTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.less = less


    # takes value, returns node with key value
    def insert(self, k):
        pass

       # self.height = 0


   # def height(self):
    #    if self.node:
     #       return self.node.height
      #  else:
       #     return 0
            
    def is_leaf(self):
        return (self.root.right | self.root.left)
    

    def balanceFactor(self):
        
        height_right = 0
        height_left = 0

        if self.root.right:
            height_right = height_right + 1 + self.root.right.balanceFactor
            
            
        if self.root.left:
            height_left = height_left + 1 + self.root.left.balanceFactor

        if self.is_leaf:
            return 0
            
        return (height_right - height_left)

    

    def right_rotate(self):
        x = self.root
        y = self.root.left
        p = y.right

        self.root = y
        y.right = x
        x.left = p

    def left_rotate(self):
        x = self.root
        y = self.root.right
        p = y.left

        self.root = x
        y.left = x
        x.right = p



    def rebalance(self):
        if self.is_leaf:
	    	return None
	    
        while self.balanceFactor > 1 or self.balanceFactor < -1:

            if self.balanceFactor > 1:
                if self.node.left.balance <0:
                    self.node.left.left_rotate()
                self.right_rotate()

            if self.balanceFactor < -1:
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                self.left_rotate()

    	return None	

    # takes value, returns node with key value
    def insert(self, k):
        
       
        if self.root is None:
            self.root = AVLNode(k)
            self.rebalance()
            return self.root

        if self.root.key == k:
            self.rebalance()
            return self.root
            
        if self.less(self.root.key, k):
            if self.root.right is None:
                self.root.right = AVLNode(k, self.root)
                self.rebalance()
                return self.root.right
            else:
                AVLTree(self.root.right).insert(k)

        else:
            if self.root.left is None:
                self.root.left = AVLNode(k, self.root)
                self.rebalance()
                return self.root.left

            else: 
                AVLTree(self.root.left).insert(k)



    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n):

        if n is None:
		  return None

        elif n.right:
            n = n.right
            while n.left:
                n = n.left  
            return n
            
        tmp = n.parent
        while tmp:
            if tmp.parent > n.parent:
                return n.parent
            tmp = tmp.parent
        
        return None      

    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
	
        if n is None:
            return None
    	elif n.left:
            n = n.left
            while n.right:
                n = n.right
            return n
        
        tmp = n.parent
        while tmp:
            if tmp.parent < n.parent:
                return n.parent
            tmp = tmp.parent
        
        return None


    # takes key returns node
    # can return None
    def search(self, k):

        if self.root.key is None:
            return None
        
        ## check if the key is already the node
        if k == self.root.key:
            return self.root
        ## recursively call the key until you find it or it doesn't 
        ## exsist, in which case return none

        if self.root.left:
            if self.less(k, self.root.key):
                return AVLTree(self.root.left).search(k)

        if self.root.right:    
                return AVLTree(self.root.right).search(k)
        else:
            return None
        
       
    # takes node, returns node
    def delete_node(self, n):
    	
        if n is None:
            return None    	
            
        new = self.predecessor(n)
        if new:
            n.key = new.key
            new.key = None
            
            extra = new.left
            if new.left:
                self.delete_node(extra)
                self.insert(extra.key)
            self.rebalance()
            return n
                
        elif self.successor(n).key:
            n.key = self.successor(n).key
            n.left = self.successor(n).left
            n.right = self.successor(n).right
            self.rebalance()
            return n
        
        else: 
            n.key = None
            n.left = None
            n.right = None
	    self.rebalance()
            return n
            

