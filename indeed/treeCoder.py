class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class TreeCoder:
    def __init__(self):
        pass

    def tree2Array(self, root):
        A = [0]
        def _dfs(node, i):
            if node is None:
                return
            if i >= len(A):
                A += [0] * len(A)
            A[i] = node.val
            _dfs(node.left, 2*i+1)
            _dfs(node.right, 2*i+2)
        _dfs(root, 0)
        return A

    def tree2Str(self, root):
        ans = ""
        def _dfs(node):
            if node is None:
                ans += "X"
                return
            ans += node.val
            _dfs(node.left)
            _dfs(node.right)
        return ans

    def str2Tree(self, s):
        if len(s) == 0:
            return
        if s[0] == 'X':
            return None
        val = int(s[0])
        node = Node(val)
        s = s[1:]
        node.left = self.str2Tree(s)
        node.right = self.str2Tree(s)

        return node

        
            
