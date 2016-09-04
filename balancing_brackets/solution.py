def isbal(st):
    if not isinstance(st, str):
        raise ValueError("input must be a string")

    braks = {'[':{}, '(':{}, '{':{}}
    brConvert = {'}':'{', ')':'(', ']':'['}
    lvl = 0
    for c in list(st):
        if c in ['[', '(', '{']:
            braks[c].setdefault(lvl, 0)
            braks[c][lvl] += 1
            lvl += 1
        elif c in [']', ')', '}']:
            lvl -= 1
            c = brConvert[c]
            braks[c].setdefault(lvl, 0)
            braks[c][lvl] -= 1

    for b, v_lv in braks.items(): # note the python2 python3 differences here with iteritems
        for k_lv, v in v_lv.items():
            if v != 0:
                return False

    return True
