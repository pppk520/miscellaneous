# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        if not A:
            return 0

        self.max_sum = -9999999999

        self.recur(A)

        return self.max_sum

    def recur(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            self.max_sum = max(self.max_sum, root.val)
            return root.val

        left_max = self.recur(root.left)
        right_max = self.recur(root.right)
        
        self.max_sum = max(self.max_sum, 
                           left_max + root.val,
                           right_max + root.val, 
                           root.val,
                           left_max + right_max + root.val)

        return max(left_max, right_max) + root.val


if __name__ == '__main__':
    assert(Solution().maxPathSum(None) == 0)

    '''
           1
    '''
    root = TreeNode(1)
    assert(Solution().maxPathSum(root) == 1)

    '''
         -100
          / 
         10  
        /  \ 
      20  -400 
    '''
    root = TreeNode(-100)
    root.left = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(-400)
    assert(Solution().maxPathSum(root) == 30)


    '''
         -100
          / 
       -200  
        /  \ 
      -300 -400 
    '''
    root = TreeNode(-100)
    root.left = TreeNode(-200)
    root.left.left = TreeNode(-300)
    root.left.right = TreeNode(-400)
    assert(Solution().maxPathSum(root) == -100)



    '''
           1
          / \
         2   3
        /   / \
       7 100  100
    '''
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert(Solution().maxPathSum(root) == 6)


    root.left.left = TreeNode(7)
    root.right.left = TreeNode(100)
    root.right.right = TreeNode(100)
    assert(Solution().maxPathSum(root) == 203)
    


