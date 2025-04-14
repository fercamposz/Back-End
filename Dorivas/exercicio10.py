inicio = int(input("digite o início do intervalo: "))
fim = int(input("digite o fim do intervalo: "))

print("numeros de Kaprekar no intervalo:")
for i in range(inicio, fim + 1):
    k2 = i * i
    k3 = str(k2)
    for k4 in range(1, len(k3)):
        esquerda = int(k3[:k4])
        direita = int(k3[k4:])
        if direita > 0 and esquerda + direita == i:
            print(i)
            break
