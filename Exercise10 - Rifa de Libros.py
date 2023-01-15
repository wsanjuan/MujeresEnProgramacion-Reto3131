n , m= map(int, (input().split()))
resultados=[]
resultado = ''
cont=1

for i in range (0,n):
    palabra= str(input())
    for letra in palabra:
        if letra == "x":
            resultado = resultado + str(cont)
            cont = cont+1
            if cont == 10:
                cont = 1
        else:
            resultado = resultado + '.'
    resultados.append(resultado)
    resultado =''

for i in resultados:
    print(i, end='\n')