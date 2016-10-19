def get_combos(coins, amt):
    if amt == 0:
        return 0
    n = 0
    for c in coins:
        ccopy = coins[:]
        ccopy.remove(c)
        n, rem = divmod(amt, c)
        if rem == 0:
            n += 1
        for i in range(n):
            aleft = amt - i * c + rem
            for c2 in ccopy:
                n += get_combos(ccopy, aleft)

    return n

if __name__ == "__main__":
    print get_combos(range(1, 4), 7) # 8
