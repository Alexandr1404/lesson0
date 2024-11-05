n = 0
m = 0
value = 0
def get_matrix(n, m, value):
    matrix = []
    n = int(input())
    m = int(input())
    value = int(input())
    for i in range (1, n+1):
        matrix.append([])
        for k in range(1, m + 1):
            matrix[i-1].append(value)
    print(matrix)

get_matrix(n, m, value)
