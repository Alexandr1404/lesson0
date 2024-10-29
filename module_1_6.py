my_dict = {'Sasha' : 2006, 'Stepa' : 2005, 'Veronica' : 1999}
print (my_dict)
print(my_dict.get ('Sasha'))
print(my_dict.get ('Dog'))
my_dict.update({'Misha' : 1945, 'Kirill' : 2013})
print (my_dict)
a= my_dict.pop ('Stepa')
print(a)
print(my_dict)


my_set = {1, 1, 1, 1, 5, 6, 5, (1,2,3 ),6, 5, 6, 'dog', 'cat', 'dog', 10}
print(set(my_set))
my_set.update({55, 10001})
my_set.discard(10)
print(my_set)