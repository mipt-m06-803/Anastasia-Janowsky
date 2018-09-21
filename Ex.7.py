n = int(input('Введите число '))
l = [2, 3, 5, 7]
for i in range(len(l)):
    ost = n % l[i]
    if ost == 0 and n != l[i]:
        print('Число составное')
        break
if ost!=0:
    print('Число простое')
