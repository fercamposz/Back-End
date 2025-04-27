n = input("Quantos termos da sequência de Fibonacci você quer? ")

if n.isdigit():
    n = int(n)
    a, b = 0, 1

    print("Sua sequência é:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
else:
    print("INVALIDO")
