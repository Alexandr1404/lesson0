calls = 0
def count_calls():
    global calls
    calls += 1

def string_info():
    count_calls()
    string = input()
    a = list()
    a.append(str(len(string)))
    a.append(str.upper(string))
    a.append(str.lower(string))
    a = tuple(a)
    print(a)


def is_contains():
    i = 0
    j = 0
    list_to_search = []
    listt = []
    count_calls()
    string = str(input())
    list_to_search = input().split()
    print(list_to_search)
    string.lower()
    ss = len(list_to_search)
    for i in list_to_search:
        listt.append(i.lower())
    for j in range(ss):
        if string == listt[j-1]:
            print(True)
        else:
            print(False)

string_info()
is_contains()
print(calls)