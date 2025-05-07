
# Exercício 2
produto_a = 5.00 * 2
produto_b = 8.00 * 2
produto_c = 12.00 * 2

print("Produto A:", produto_a)
print("Produto B:", produto_b)
print("Produto C:", produto_c)

# Exercício 3
numeros = [4, 7, 10]
for num in numeros:
    if num % 2 == 0:
        print(f"{num} é par (jogador avança)")
    else:
        print(f"{num} é ímpar (jogador recua)")

# Exercício 4
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")
for i in range(1, 11):
    print(f"4 x {i} = {4 * i}")

# Exercício 5
idades = [8, 15, 20]

for idade in idades:
    if idade >= 18:
        print(f"Cliente de {idade} anos pode assistir ao filme")
    else:
        print(f"Cliente de {idade} anos n pode assistir ao filme")

# Exercício 6
produto1 = 50.00 * 0.9
produto2 = 120.00 * 0.9
produto3 = 200.00 * 0.9
print("Produto 1:", produto1)
print("Produto 2:", produto2)
print("Produto 3:", produto3)

# Exercício 7
palavras = ["casa", "paralelepípedo", "python"]
for palavra in palavras:
    print(f"A palavra '{palavra}' tem {len(palavra)} letras")

# Exercício 8
temp = [30, 100, 0]
for celsius in temp:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")

# Exercício 9
numeros = [3, 9, 12]
for num in numeros:
    if num <= 5:
        print(f"O número {num} é pequeno.")
    elif num <= 10:
        print(f"O número {num} é médio.")
    else:
        print(f"O número {num} é grande.")

# Exercício 10 (não entendi..)
titulos = ["Ana Ana", "1DSTB-SENAI", "Subi no Onibus"]
for titulo in titulos:
    titulo = titulo.replace(" ", "").lower()
    if titulo == titulo[::-1]:
        print(f"'{titulos}' é um palíndromo")
    else:
        print(f"'{titulos}' não é um palíndromo")

# Exercício 11
numeros = [3, 7, 9, 25, 26]
fatoriais = []

for num in numeros:
    fatorial = 1
    while num > 1:
        fatorial *= num
        num -= 1
    fatoriais += [fatorial]

print(f"O fatorial de {numeros[0]} é {fatoriais[0]}.")
print(f"O fatorial de {numeros[1]} é {fatoriais[1]}.")
print(f"O fatorial de {numeros[2]} é {fatoriais[2]}.")
print(f"O fatorial de {numeros[3]} é {fatoriais[3]}.")
print(f"O fatorial de {numeros[4]} é {fatoriais[4]}.")