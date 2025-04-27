num = input("Digite um número: ")

if num.isdigit():
    num = int(num)
    fatorial = 1
    contador = ""

    for i in range(num, 0, -1):
        fatorial *= i
        if i == 1:
            contador += f"{i} "
        else:
            contador += f"{i} x "

    print(f"{num}! = {contador}= {fatorial}")
else:
    print("INVALIDO")
