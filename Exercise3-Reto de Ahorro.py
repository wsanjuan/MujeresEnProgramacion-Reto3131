n=int(input())

if n%2==0:
  resultado=(n+1)*(n/2)
else:
  resultado=(n+1)*(n//2)+(n//2)+1

print(int(resultado))