l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = []
def transpose(l1, l2):
    for i in range(len(l1[0])):
        row = []
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2

print(transpose(l1, l2))


