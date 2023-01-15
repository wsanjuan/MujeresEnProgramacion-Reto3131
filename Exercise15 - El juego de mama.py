a , b, c, d= map(int, (input().split()))

if a*b*c*d<=250:
    print (a*b*c*d)
else:
    if 10 in (a, b, c, d):
        resultado = b*c*d
    else:
        resultado = a*b*c

    if resultado > 250:
        print('pierdes')
    else:
        print(resultado)