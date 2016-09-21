def is_sum_n2(arr, n):
    for i in arr:
        for i2 in arr:
            if i + i2 == n:
                return True
    return False

from itertools import combinations
def is_sum(arr, n):
    combos = combinations(arr, 2)
    for c in combos:
        if sum(c) == n:
            return True

    return False

if __name__ == "__main__":
    arr = [1, 3, 4, 7]
    n = 11
    print is_sum_n2(arr, n)
    print is_sum(arr, n)
    arr2 = [1, 3, 3, 7]
    print is_sum_n2(arr2, n)
    print is_sum(arr2, n)
