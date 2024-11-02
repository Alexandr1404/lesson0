my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
b = len(my_list)
while b != 0:
    c = my_list.pop(0)
    if c == 0:
        continue
    if c > 0:
        print(c)
    if c < 0:
        break
    b = len(my_list)