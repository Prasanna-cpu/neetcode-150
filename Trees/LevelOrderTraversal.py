#
#
# Binary Tree Level Order Traversal
# Solved
# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4,5,6,7]
#
# Output: [[1],[2,3],[4,5,6,7]]
# Example 2:
#
# Input: root = [1]
#
# Output: [[1]]
# Example 3:
#
# Input: root = []
#
# Output: []
# Constraints:
#
# 0 <= The number of nodes in both trees <= 1000.
# -1000 <= Node.val <= 1000

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result

