num = int(input("digite o numero de termo:"))
soma = 0
for i in range(1, num + 1):
    soma += 1/ i

print(f"a soma da serie harmônica é:{soma:.2f}")