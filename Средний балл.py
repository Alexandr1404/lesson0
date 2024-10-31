from typing import Dict

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_ = list (students)
list_.sort()
list2 = list (grades)

names = []
a=(grades.pop(0))
s=str(sum(a)/len(a))
b=list_.pop(0)

book = []
book.append(float(s))
names.append(b)

a=(grades.pop(0))
s=str(sum(a)/len(a))
book.append(float(s))
b=list_.pop(0)
names.append(b)


a=(grades.pop(0))
s=str(sum(a)/len(a))
book.append(float(s))
b=list_.pop(0)
names.append(b)


a=(grades.pop(0))
s=str(sum(a)/len(a))
book.append(float(s))
b=list_.pop(0)
names.append(b)


a=(grades.pop(0))
s=str(sum(a)/len(a))
book.append(float(s))
b=list_.pop(0)
names.append(b)

names1 = list(names)
book1 = list(book)
truelist_: dict[str, str] = dict(zip(names1, book1))
print(truelist_)

