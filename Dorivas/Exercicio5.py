num = int(input("digite um numero:"))

contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

if contador == 2:
        print(f"{num} é primo")
else:
        print(f"{num}não é primo")