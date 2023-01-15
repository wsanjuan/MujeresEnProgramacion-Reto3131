n= int(input())
cortes= {
    range(0,99):'No insignia',
    range(100,499):'Bronce',
    range(500,999):'Plateada',
}

if n < 1000:
    for key in cortes.keys():
        if n in key:
            print(cortes[key])
else:
    print("Dorada")