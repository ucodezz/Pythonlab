num = int(input('enter a number'))
res = 0
while(num != 0):
    res += num % 10
    num = int(num / 10)
print(res)


# ANOTHER WAYY

# def sum(val):
#     sum = 0
#     for i in str(val):
#         sum += int(i)
#     print('the sum of ', val, ' is', sum)

# n=int(input("enter eny digit"))
# sum(n)