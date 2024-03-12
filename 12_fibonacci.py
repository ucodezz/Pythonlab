# Write a program to obtain the first n numbers of a Fibonacci sequence. n should be read from user.  

# ITERATIVE METHOD
num = int(input('enter number to get fibonacci series'))
a = 0
b = 1
# print(num)
print(a)
print(b)


for i in range(1, num-1):
    c = a + b
    print(c)
    a = b
    b = c


l1 = ['apple', 'banana']
[print(x,end=" ") for x in l1 for i in range(0,5)]

