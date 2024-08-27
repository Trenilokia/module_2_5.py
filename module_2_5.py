def get_matrix(n, m, value):
    matrix = []
    lst_m = []
    for i in range(n):
        matrix.append(lst_m)
        for k in range(m):
            lst_m.insert(i, value)
            if int(len(lst_m) == m):
                lst_m = []
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)