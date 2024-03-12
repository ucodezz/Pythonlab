l1 = [[2,3,4],[5,6,7],[88,7,6]]
l2 = [[3,76,5],[3,54,0],[1,0,1]]
l3 = [[0,0,0],[0,0,0],[0,0,0]]

# row, col = [0,0]
# l3 = [[0]*col]*row
# print(l3)

# ADDITION
# for i in range(len(l1[0])):
#     for j in range(len(l2[0])):
#         l3[i][j] = l1[i][j] + l2[i][j]
# print(f'the sum of 2 matrix is :', l3)

# QUESTION 25  MULTIPLICATION
for i in range(len(l1[0])):
    for j in range(len(l2[0])):
        for k in range(len(l3[0])):
            l3[i][j] += l1[i][k] * l2[k][j]

print(l3)