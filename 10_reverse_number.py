num = int(input('enter a number\n'))
rev = 0
while(num != 0):
    res = num % 10
    rev = rev * 10 + res
    num = int(num / 10)
print(rev)