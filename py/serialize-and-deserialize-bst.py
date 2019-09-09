# We did it in 2n bits!

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def __init__(self):
        self.struct, self.data = [], []

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # If root is None, put 0 in structure array and return
        if root is None:
            self.struct.append(0)
            return
      
        # Else place 1 in structure array, val in 'data' array
        # and recur for left and right children
        self.struct.append(1)
        self.data.append(root.val)
        self.serialize(root.left)
        self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if len(self.struct) < 1:
            return None

        # Remove one item from structure list 
        b = self.struct[0] 
        self.struct.pop(0) 
          
        # If removed bit is 1 
        if b == 1:  
            val = self.data[0] 
            self.data.pop(0) 
          
            #Create a tree node with removed data 
            root = TreeNode(val) 
      
            #And recur to create left and right subtrees 
            root.left = self.deserialize(self.data); 
            root.right = self.deserialize(self.data); 
            return root 
      
        return None
 
    # Preorder traversal to print
    def preorder(self, root): 
        if root: 
            print(f'val: {root.val}', end=' | ')
                  
            if root.left:
                print(f"left child -->: {root.left.val}", end=' ')
            if root.right:
                print(f"right child --> {root.right.val}", end=' ')
            print()
            self.preorder(root.left)
            self.preorder(root.right)


# Build tree manually for testing
root = TreeNode(10)
root.left = TreeNode(20) 
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.right = TreeNode(70)

print("Given Tree")
codec = Codec()
codec.deserialize(codec.serialize(root))
codec.deserialize(codec.serialize(root))
  
codec.preorder(root)

codec.serialize(root)
print("\nEncoded Tree")
print("Structure List")
  
for i in codec.struct:
    print(i, end=' ')

print("\nDataList")
for value in codec.data:
    print(value, end=' ')
  
newroot = codec.deserialize(codec.data) 
  
print("\n\nPreorder Traversal of decoded tree")
codec.preorder(newroot)
# Your Codec object will be instantiated and called as such:
# codec = Codec()