'''TWP293 Fatorial Função e Globais vs Locais
       '''

def fat(n):
    f=1
    while n >0:
        f = f * n
        n = n - 1
    return f
n= int(input("Digite um numero inteiro: "))
print(fat(n))