immutable_var = 1, 10, True, 'Moscow'
print (immutable_var)
immutable_var = [1, 10], True, 'Moscow'
# Если задать кортеж, то не получается изменить элементы
# Если добавить в кортеж список, то можно изменить его, т.е. список - изменяемый объект
print (immutable_var)
immutable_var [0] [1] = 9
print (immutable_var)
mutable_list = [1, 10, True, 'Moscow']
print (mutable_list)
mutable_list [1] = 'Owl'
print (mutable_list)