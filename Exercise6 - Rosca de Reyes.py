n=int(input())
resultado = [0, 0]

for i in range (0,n):
    x = int(input())
    resultado[0] = resultado[0] + (2*x)
    resultado[1] = resultado[1] + (3*x)

print(' '.join(map(str, resultado)))