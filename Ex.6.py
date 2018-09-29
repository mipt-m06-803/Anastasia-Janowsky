N = int(input('Vvedite N '))
l = []
l.append(int(input()))
n = l[0]
for i in range(N-1):
    i = int(input())
    if i > n:
        n = i
print(n)
