"""
Unique Binary Search Trees II
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
"""
class Solution(object):
    def generateTrees(self, n):
        def build(start, end):
            if start > end:
                return [None]

            result = []

            for root in range(start, end + 1):
                left = build(start, root - 1)
                right = build(root + 1, end)

                for l in left:
                    for r in right:
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        result.append(node)

            return result

        return build(1, n)