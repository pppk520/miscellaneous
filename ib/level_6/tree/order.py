class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SegTree:
    def __init__(self, n):
        self.n = n
        self.root = TreeNode(0)

    def occupy(self, root, base, idx, node_num):
        if node_num == 1:
            return TreeNode(-1) # terminal

        if root == None:
            root = TreeNode(0)

        root.val += 1
        mid = node_num / 2
        if idx < mid:
            root.left = self.occupy(root.left, base, idx, mid)
        else:
            root.right = self.occupy(root.right, base + mid, idx - mid, node_num - mid)

        return root

    def get_ith_empty(self, root, base, idx, node_num):
        if not root or root.val == -1:
            return base + idx - 1 # zero index

        remain = node_num - root.val
        if remain < idx:
            return

        mid = node_num / 2

        if not root.left:
            left_remain = mid
        elif root.left.val == -1:
            left_remain = 0
        else:
            left_remain = mid - root.left.val

        if left_remain >= idx:
            return self.get_ith_empty(root.left, base, idx, mid)
        else:
            return self.get_ith_empty(root.right, base + mid, idx - left_remain, node_num - mid)

class Solution:
    # @param heights : list of integers
    # @param infronts : list of integers
    # @return a list of integers
    def order(self, heights, infronts):
        d = {}
        st = SegTree(len(heights))

        for i in range(len(heights)):
            d[heights[i]] = infronts[i]

        arr = [None] * len(heights)
        for i, h in enumerate(sorted(d)):
            idx = st.get_ith_empty(st.root, 0, d[h] + 1, st.n)

            arr[idx] = h
            st.occupy(st.root, 0, idx, st.n)

        return arr

if __name__ == '__main__':
    print(Solution().order([5, 3, 2, 6, 1, 4], [0, 1, 2, 0, 3, 2])) # 5 3 2 1 6 4
    print(Solution().order([11, 42, 29, 73, 21, 19, 84, 37], [6, 2, 0, 0, 5, 5, 0, 0])) # 29 37 73 84 42 19 11 21 
    print(Solution().order([29, 82, 30, 62, 23, 67, 35], [5, 0, 2, 0, 3, 1, 1])) # 62 35 30 23 82 67 29 
