num = int(input("Digite um numero:"))

soma = 0
contador = 0

while contador <= num:
    soma += contador
    contador += 1

print(f"A soma de 1 até {num} é: {soma}")
