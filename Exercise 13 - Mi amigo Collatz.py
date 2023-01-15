n = int(input())
resultado = n
numeros=[n]

while resultado >1:
    if resultado%2 == 0:
        resultado = resultado/2
    else:
        resultado = (resultado * 3)+1
    numeros.append(int(resultado))

print(' '.join(map(str, numeros)))




