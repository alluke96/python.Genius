import random
from time import sleep

pontos = 0
listadecores = ['1','2','3','4']
tentativa = ['1','2','3','4']
s = 0


def cls():
    print('\n' * 50)

for r in range(0, 4, 1):
    listadecores[r] = random.choice(listadecores)

for m in range(0, 4, 1):
    print(listadecores[m])
    sleep(1)
    cls()

print('')
sleep(2)

for i in range(len(listadecores) + s):
    tentativa[i] = input("Digite sua tentativa: ")
    if tentativa[i] == listadecores[i]:
        pontos += 1
    else:
        print("Voce errou!")
        print("Pontos:", pontos)
        exit()

print("Voce ganhou!")
s += 1
print("Pontos:", pontos)
