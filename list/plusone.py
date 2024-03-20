def plusOne(digits):
    lst = digits[:]

    for i in range(len(lst)-1, -1, -1):
        if lst[i] != 9:
            lst[i] = lst[i] + 1
            break
        if lst[i] == 9:
            lst[i] = 0
            if i == 0:
                lst.insert(0, 1)
                break
            continue

    return lst


lst = [9, 9, 9, 9]
print(plusOne(lst))