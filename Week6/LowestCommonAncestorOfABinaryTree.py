# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q found in different subtrees, root is LCA
        if left and right:
            return root

        # Otherwise, LCA is either in left or right
        return left if left else right

def build_tree():
    nodes = {val: TreeNode(val) for val in [3,5,1,6,2,0,8,7,4]}
    nodes[3].left = nodes[5]
    nodes[3].right = nodes[1]
    nodes[5].left = nodes[6]
    nodes[5].right = nodes[2]
    nodes[1].left = nodes[0]
    nodes[1].right = nodes[8]
    nodes[2].left = nodes[7]
    nodes[2].right = nodes[4]
    return nodes[3], nodes

root, nodes = build_tree()
p = nodes[5]
q = nodes[1]

sol = Solution()
lca = sol.lowestCommonAncestor(root, p, q)
print(f"LCA of {p.val} and {q.val} is: {lca.val}")