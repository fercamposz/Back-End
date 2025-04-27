num = input("Digite o seu número: ")

if num.isdigit():
    num = int(num)
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
else:
    print("INVALIDO")
