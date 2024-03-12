# PART A
def binary_iterative(num):
    res = []
    while(num >= 1):
        res.append(num%2)
        num = int(num/2)
    res1 = res[::-1]
    string = ''
    for x in res1:
        string += str(x)
    print(string)


def binary_recursion(num):
    if(num == 0):
        return 0
    else:
        b = num % 2 + 10 *  binary_recursion(int(num/2)) 
    return b


num = int(input('enter a value\n')) 
# binary_iterative(num)
# binary_recursion(num)[::-1]

print(binary_recursion(num))

# PART B
def octal_recursion(num):
    if(num == 0):
        return 0
    else:
        b = num % 8 + 10 * octal_recursion(int(num/8))
    return b


num = int(input('enter a value\n')) 
print(octal_recursion(num))

