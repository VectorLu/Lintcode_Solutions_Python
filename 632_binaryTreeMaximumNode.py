class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    node = None
    maxNum = -99999
    
    def maxNode(self, root):
        # Write your code here
        if root is None:
            return None
        self.max(root)
        return self.node
    
    def max(self, root):
        if root is None:
            return None
        if root.val > self.maxNum:
            self.node = root
            self.maxNum = root.val
        self.max(root.left)
        self.max(root.right)