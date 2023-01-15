a , b, c= map(int, (input().split()))
respuesta='NO'
if a + b > c:
    if a + c > b:
        if c + b > a:
            respuesta = 'SI'

print(respuesta)