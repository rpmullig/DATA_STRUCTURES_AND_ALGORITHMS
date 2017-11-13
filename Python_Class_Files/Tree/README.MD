BinarySearchTree and AVLTree by Robert Mulligan - rpmullig C343 


# BST
-BSTNODE
using OOP, builds a node with key, 3 pointers and defaults to none

-Less_Than
defines a less than function to be passed into the tree object that structures the nodes together

-BinarySearchTree
object to hold the nodes with a root element that has the node in it default to none

-insert
places key in tree
  checks if blank on root, then insert
  checks if the value is already there, in which case don't add it
  uses the less function to check if node needs to go down left side of tree
    recurse till an empty slot is open
  if it's not the left side, then else it's the right side of the tree

-successor
  if no node, then there isn't one
  down the tree is simply the right node and then the furthes left most node on that subtree
  
  if no down, check upward to see if the parent's parent is greaeter then, in which case it's less
  than and thus the parent is the successor

- Predecessor
  same as successor with flipping sides and greater than to less than
  
  if no node, then there isn't one
  
  down the tree is simply the left node and then the furthes right most node on that subtree
  
  if no downward movement, then see up if the grandparent is less than the parent - in which case it's the 
  parent that is the predeccessor
  
  
-search
  if the node already there is the same as the key, return that node
  
  if not, recure down each side until  down left and right in search for the key
  
  base case is to return nothing, untill the k == self.root.key

-delete_node
  uses predecessor and places that node into the new spot while making sure it any thing
  down the left subtree of predecessor is added into the tree through a while/recursive loop
  
  if no predecessor, then use the successor
  
  if no predecessor or successor, then just change values to None
  
# AVL

Same functions just washing them through a rebalancing fucntion when returning nodes
the rebalancing function first starts with a balanceFactor function that recursively goes through
the tree and checks left to right

the other component is the rotate left and rotate right. Thses are rather conceptual and require
changing 3 variable and adjusting them around 

using a while loop through the balanceFactor with greater than 1 and less than -1, the 
tree will balance using the appropriate lef and right rotate functions and continue down the tree
till everything is balanced

I beleive this method is a top down approach and will look to rebalance starting at the top and work it's 
way down


anytime a node is returned, the rebalnace() will occur before that to return a blanaced AVL tree
