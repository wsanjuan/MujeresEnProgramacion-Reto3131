n, m, x = map(int, input().split())

if (n*m)%x ==0:
    resultado = (n*m)/x
else:
    resultado = int((n*m)/x) +1

print (int(resultado))