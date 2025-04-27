num = input("Digite um número: ")

if num.isdigit():
    num = int(num)
    for i in range(1, num + 1):
        print("*" * i)
else:
    print("INVALIDO")
