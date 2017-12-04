# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param val1 : integer
    # @param val2 : integer
    # @return an integer
    def lca(self, A, val1, val2):
        path_1 = self.dfs(A, [], val1)
        path_2 = self.dfs(A, [], val2)

        if not path_1 or not path_2:
            return -1

        min_len = min(len(path_1), len(path_2))

        for i in range(min_len):
            if path_1[i] != path_2[i]:
                return path_1[i - 1]

        return path_1[i]


    def dfs(self, root, parents, target_val):
        if not root:
            return

        if root.val == target_val:
            return parents[:] + [root.val]

        path = parents[:] + [root.val]

        ret = self.dfs(root.left, path, target_val)
        if ret:
            return ret

        ret = self.dfs(root.right, path, target_val)
        if ret:
            return ret

        return



if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    assert(Solution().lca(root, 5, 4) == 5)
    assert(Solution().lca(root, 4, 8) == 3)
    assert(Solution().lca(root, 7, 4) == 2)




