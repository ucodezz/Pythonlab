# A
a = int(input('enter the value')) #4

for i in range(a):
    for j in range(i+1):
        print("*", end='')
    print('\n')

# B
a = int(input('enter the value\n'))
j = a

for i in range(a):
    for j in range(j):
        print('*', end=' ')

        # if applying this, it will print only odd no. of starts
        # j -= 1
    print('\n')


# C
a = int(input('enter the value\n'))
j = 0
for i in range(1, a+1):
    for space in range(1, (a-i)+1):
        print(end=' ')

    while j!=(2*i-1):
        print('* ', end='')
        j += 1
    
    j = 0
    print()

 
    



