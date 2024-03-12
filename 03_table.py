#PRINT A TABLE
# def table(num):
#     for i in range(1, 11):
#         print(num, 'X', i, '=', num*i)

num = int(input('enter a value')) 
end = int(input('enter the end value'))
# table(num)


print([num*i for i in range(1, end+1)])



