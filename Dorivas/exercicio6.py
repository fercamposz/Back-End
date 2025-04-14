n = int(input("quantos termos da sequência de Fibonacci voce quer?"))
a, b = 0, 1

print("sua sequeência é")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b