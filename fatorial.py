#
#
#
num = int(input("Digite um valor inteiro e positivo: "))
i = 1
fat = 1
while i <= num:
    fat = fat * i
    i = i + 1
print ("O fatorial de eh ", num, "=", fat)