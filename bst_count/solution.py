# note: this binary search tree must be sorted by hand
class BST(object):
    def __init__(self):
        self.root = None

    def set_root(self, root):
        self.root = root

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_nodes(root):
    node_cnt = 1
    q = [root.left, root.right]
    while q:
        root = q.pop()
        if root is not None:
            node_cnt += count_nodes(root)

    return node_cnt

if __name__ == "__main__":
    root = Node(12)
    root.left = Node(6)
    root.right = Node(20)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(15)

    print count_nodes(root) # 6
