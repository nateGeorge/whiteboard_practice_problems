def unp_int():
    ints = map(int, raw_input().split(',').strip())
    ans = []
    intd = {}
    for i in ints:
        intd.setdefault(i, 0)
        intd[i] += 1
    for i, v in ints.iteritems():
        if v > 1:
            continue
        ans.append(i)
    return ans
