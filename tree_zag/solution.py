def zigzag():
    a, b, c = raw_input().split(', ')
    head = a
    n = {a: [b, c]}
    a, b, c = raw_input().split(', ')
    while a is not None:
        n[a] = [b, c]
        a, b, c = raw_input().split(', ')

    lvls = {0:head}
    i = 1
    q = [head]
    while q:
        allN = q[:]
        q = []
        for e in allN:
            q.extend(n[e])
            lvl.setdefault(i, []).extend(n[e])
        lvls[i] = [l in l != 1 for l in lvls[i]]

    i = 0
    for l in lvls:
        print lvls[l][i]
        if i == 0:
            i = -1
        else:
            i = 0
