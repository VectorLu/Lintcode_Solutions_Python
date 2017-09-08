class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    node = TreeNode(-9999)

    def maxNode(self, root):
        # Write your code here
        if root is None:
            return None
        else:
            self.max(root)
            return self.node

    def max(self, root):
        if root is None:
            return None
        if root.val > self.node.val:
            self.node = root
        self.max(root.left)
        self.max(root.right)
        
