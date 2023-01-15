n , m= map(int, (input().split()))

for i in range (0,m):
    x , y= map(int, (input().split()))
    n = n-(y-x+1)

print(n)