'''
#1ts
import math as m

carpet = list(map(int, input().split(sep='x')))
sqr_ar = 13
if (sqr_ar >= carpet[1] and sqr_ar-carpet[1] >= carpet[0]) or (sqr_ar >= carpet[0] and sqr_ar-carpet[0] >= carpet[1]):
    print('да')
else:
    print('нет')

#2nd
hole_size = list(map(int, input().split(sep='x')))
brick_size = list(map(int, input().split(sep='x')))

sides = 0
for i in brick_size:
    if hole_size[0] >= i:
        sides+=1
for i in brick_size:
    if hole_size[1] >= i:
        sides+=1

if sides >= 2:
    print('да')
else:
    print('нет')

#3rd
nbr = list(map(int, input().split(sep='x')))
K = int(input())

dev_nbr = []
for i in range(1, nbr[0]):
    dev_nbr.append(i*nbr[1])


if K in dev_nbr:
    print('успешно')
else:
    for i in range(1, nbr[1]):
        dev_nbr.append(i * nbr[0])
    if K in dev_nbr:
        print('успешно')
    else:
        print('неосуществимо')

letters = ['a', 'b', 'c', 'd', 'i', 'f', 'g', 'h']
nummers = ['1', '2', '3', '4', '5', '6', '7', '8']
chess_desk = {}

q = [1, 1]
for i in letters:
    for k in nummers:
        if q[0]%2 != 0 and q[1]%2 != 0:
            chess_desk[f'{i}{k}'] = 'черный'
        elif q[0]%2 != 0 and q[1]%2 == 0:
            chess_desk[f'{i}{k}'] = 'белый'
        elif q[0] % 2 == 0 and q[1] % 2 != 0:
            chess_desk[f'{i}{k}'] = 'белый'
        elif q[0] % 2 == 0 and q[1] % 2 == 0:
            chess_desk[f'{i}{k}'] = 'черный'
        q[0]+=1
        if q[0]==9:
            q[1]+=1
            q[0]=1

chess_inp = input()
print(chess_desk.get(chess_inp.lower(), None))

horse_step = list(input().split(sep='-'))

letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'i': 5, 'f': 6, 'g': 7, 'h': 8}
nummers = ['1', '2', '3', '4', '5', '6', '7', '8']
quot = []
for i in letters.keys():
    for k in nummers:
        quot.append(f'{i}{k}')


first_let = letters.get(horse_step[0][0])
second_let = letters.get(horse_step[1][0])


if abs(int(horse_step[0][1])-int(horse_step[1][1])) == 2 and abs(first_let - second_let)==1:
    print('верно')
elif abs(int(horse_step[0][1])-int(horse_step[1][1])) == 1 and abs(first_let - second_let)==2:
    print('верно')
else:
    print('ошибка')

print(first_let, second_let)

#6th
atr = list(map(int, input().split()))
print(round(atr[2]*(atr[0]*2)/atr[1]))

#7th
Q = int(input())
if ((Q%5)+5)//7 == 0:
    print('да')
else:
    print('нет')

import random

#8th
num = []
for i in range(1,201):
    num.append(i)

subseq = {1: 0}

for i in range(2,201):
    k = random.choice(num)
    subseq[i] = k
    num.remove(k)

while True:
    print(subseq.get(int(input())))
    if input() == 'exit': break
'''
