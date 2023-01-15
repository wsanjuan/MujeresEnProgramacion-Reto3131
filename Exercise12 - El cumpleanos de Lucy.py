n = int(input())
palabras=['casa', 'parque', 'alberca', 'sabado', 'domingo']
resultado1=[0,0,0]
resultado2=[0,0]


for i in range(0, n):
    a, b = map(int, (input().split()))
    resultado1[a-1] = resultado1[a-1] + 1
    resultado2[b-1] = resultado2[b-1] + 1

maximo=max(resultado1)
for i in range(0, len(resultado1)):
    if resultado1[i]==maximo:
        lugar = palabras[i]

maximo=max(resultado2)
for i in range(0, len(resultado2)):
    if resultado2[i]==maximo:
        dia = palabras[i+3]

print(lugar + ' ' + dia)