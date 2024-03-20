def plusOne(digits):
    lst = digits[:]

    for i in range(1, len(lst)+1):
        if lst[-i] != 9:
            lst[-i] = lst[-i] + 1
            break
        if lst[-i] == 9:
            lst[-i] = 0
            if i == len(lst):
                lst.insert(0, 1)
                break
            continue

    return lst


lst = [9, 9, 9, 9]
print(plusOne(lst))