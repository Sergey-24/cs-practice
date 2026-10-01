porog = float(input())
n = int(input())
cheter = 0
chethg = 0
max1 = -10**10
crz = 0
orc = 0
for i in range(n):
    new = input()
    if new == 'error':
        cheter+=1
    else:
        neer = float(new)
        if neer>porog:
            chethg+=1
        if max1<neer:
            max1=neer
        crz += neer
        orc+=1
crz/= orc
print(f'Всего записей: {n}')
print(f'Количество error: {cheter}')
print(f'Количество превышений:{chethg}')
print(f'Максимальное значение:{max1:.1f}')
print(f'Среднее показание:{crz:.1f}')
