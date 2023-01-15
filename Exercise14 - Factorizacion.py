n = int(input())
cont=0
sqr=int(n**(1/2))
x=2
while n!=1 and x<=sqr:
    while n%x==0:
        cont=cont+1
        n=n/x
    if cont > 0:
        print(str(x) + ' ' + str(cont))
        cont=0
    x=x+1

if n==1:
    pass
else:
    print(str(int(n)) + ' ' + '1')

