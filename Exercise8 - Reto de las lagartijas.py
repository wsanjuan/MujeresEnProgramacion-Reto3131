m , l= map(int, (input().split()))
list = list(map(int, input().split()))
resultado = (list[0]-1)//l

for i in range (0,m-1):
    resultado = resultado + (((list[i+1]-list[i])-1)//l)

print (resultado)