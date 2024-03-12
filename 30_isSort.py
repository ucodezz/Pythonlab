l1 = []
count = False
while(True):
    a = int(input('enter to value to enter in list'))
    if a < 0:
        break
    else:
        l1.append(a)

for i in range(len(l1)):
    if l1[i+1] > l1[i] and l1[0] < l1[-1]:
        count = True
    else:
        count = False

if(count == True):
    print('sorted')
else:
    print('not sorted')
