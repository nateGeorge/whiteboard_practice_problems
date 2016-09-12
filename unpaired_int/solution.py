def ret_unp(inputStr):
    nums = map(int, inputStr.split(','))
    nums = sorted(nums)
    for i in range(0, len(nums) / 2, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
        if len(nums) % 2 != 0:
            return nums[-1]
    return None

if __name__ == '__main__':
    test1 = '1, 2, 3, 1, 2'
    print ret_unp(test1) # 3
    test2 = '1, 2, 3, 4, 5, 99, 1, 2, 3, 4, 5'
    print ret_unp(test2) # 99
