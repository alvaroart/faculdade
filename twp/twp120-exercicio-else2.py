
minutos= int(input("Minutos utilizados: "))
if minutos < 200:
    conta = 0.20
else:
    if minutos <= 400:
        conta=0.18
    elif:
        conta = 0.15
    else minutos < 800:
        conta = 0.08
print("conta: R$ %6.2f" %(minutos*conta))