def get_tree_h(tree):
    if not isinstance(tree, BST):
        raise ValueError("input must be a binary search tree")

    h = 0
    curnodes = [tree.head]
    nextnodes = []
    while len(curnodes) > 0:
        for n in curnodes:
            if n.right:
                nextnodes.append(n.right)
            if n.left:
                nextnodes.append(n.left)
        curnodes = nextnodes[:]
        nextnodes = []
        h += 1

    return h - 1
