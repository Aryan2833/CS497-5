class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    def in_order_traversal(node):
        nonlocal prev, min_diff
        if not node:
            return

        in_order_traversal(node.left)

        if prev is not None:
            min_diff = min(min_diff, abs(node.val - prev))
        prev = node.val

        in_order_traversal(node.right)

    prev = None
    min_diff = float('inf')

    in_order_traversal(root)

    return min_diff

# Test cases
root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(getMinimumDifference(root1))

root2 = TreeNode(1, None, TreeNode(48, None, TreeNode(12, None, TreeNode(49))))
print(getMinimumDifference(root2))
