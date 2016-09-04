def rot(arr, st):
    if not isinstance(arr, list):
        raise ValueError("first argument must be a list")
    if not isinstance(st, int):
        raise ValueError("second argument must be an int")
    st = st % len(arr)
    if st == 0:
        return arr
    fst = arr[-st:]
    lst = arr[:-st]
    return fst + lst
