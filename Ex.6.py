N = int(input('Vvedite N '))
l = []
for _ in range(N):
    l.append(int(input()))
    n1 = l[0]
    for n2 in l[1:]:
        if n2 > n1:
            n1 = n2
print(n1)
