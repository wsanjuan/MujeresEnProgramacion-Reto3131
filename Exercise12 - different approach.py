n = int(input())

lugares= [[1, 'casa', 0],[2, 'parque', 0],[3, 'alberca', 0]]
dias= [[1, 'sabado', 0],[2, 'domingo', 0]]


for i in range(0, n):
    a, b = map(int, (input().split()))
    for i in range(0,len(lugares)):
        if lugares[i][0] == a:
            lugares[i][2] = lugares[i][2] + 1
    for i in range(0, len(dias)):
        if dias[i][0] == b:
            dias[i][2] = dias[i][2] + 1

resultado=[]

for list in [lugares, dias]:
    max = 0
    pointer = 0
    for i in range(0, len(list)):
        if list[i][2] > max:
            max = list[i][2]
            pointer = i
    resultado.append(list[pointer][1])

print(resultado[0] + ' ' + resultado[1])