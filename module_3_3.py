values_list = [1, 'asfa', False]
values_dict = {'a' : 'pen', 'b' : True, 'c' : 45}
values_list_2 = ['king', 89]
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 78)
