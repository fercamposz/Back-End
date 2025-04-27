num = input("Digite o número de termos: ")

if num.isdigit():
    num = int(num)
    soma = 0
    for i in range(1, num + 1):
        soma += 1 / i

    print(f"A soma da série harmônica é: {soma:.2f}")
else:
    print("INVALIDO")
