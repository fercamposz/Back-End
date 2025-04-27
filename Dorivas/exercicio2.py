num = input("Digite um número: ")

if num.isdigit():
    num = int(num)
    soma = 0
    contador = 0

    while contador <= num:
        soma += contador
        contador += 1

    print(f"A soma de 1 até {num} é: {soma}")
else:
    print("INVALIDO")
