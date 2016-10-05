def get_change(coins, amt):
    if not isinstance(coins, list):
        raise ValueError("coins must be a list")

    c_cnts = []
    for c in sorted(coins, reverse=True):
        n, amt = divmod(amt, c)
        c_cnts.append(n)

    return sum(c_cnts), c_cnts[::-1]

if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amt = 42
    print get_change(coins, amt) # 5, [2, 1, 1, 1]
    print get_change(coins, 12)
