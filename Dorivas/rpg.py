import random

print("★★★ RPG ★★★")

modo = input("Escolha como vc deseja jogar: [1] singleplayer (contra CPU) | [2] multiplayer: ")

jogador1 = input("Digite o nome do Jogador 1: ")

if modo == "1":
    jogador2 = "CPU"
else:
    jogador2 = input("Digite o nome do Jogador 2: ")

hp_jogador1 = random.randint(200, 1000)
atq_jogador1 = random.randint(1, 50)
def_jogador1 = random.randint(1, 50)

hp_jogador2 = random.randint(200, 1000)
atq_jogador2 = random.randint(1, 50)
def_jogador2 = random.randint(1, 50)

turno = 1
while hp_jogador1 > 0 and hp_jogador2 > 0:
    print(f"\n★★★ Turno {turno} ★★★")
    print(f"{jogador1} - HP: {hp_jogador1}")
    print(f"{jogador2} - HP: {hp_jogador2}")

    if turno % 2 != 0:
        print(f"\nTurno de {jogador1}")
        print("[1] Atacar")
        print("[2] Curar")
        acao = input("Escolha : ")  #ate aqui ta certo

        if acao == "1":
            critico = random.randint(1, 100) <= 10
            dano_base = max(1, atq_jogador1 - def_jogador2)
            dano = dano_base * 2 if critico else dano_base
            hp_jogador2 -= dano
            if critico:
                print("dano dobrado!")
            print(f"{jogador1} atacou {jogador2} e causou {dano} de dano")
        elif acao == "2":
            cura = 20
            hp_jogador1 += cura
            print(f"{jogador1} se curou em {cura} HP!")
    else:
        print(f"\nTurno de {jogador2}")
        if modo == "1":
            acao = random.choice(["1", "2"])
            if acao == "1":
                critico = random.randint(1, 100) <= 10
                dano_base = max(1, atq_jogador2 - def_jogador1)
                dano = dano_base * 2 if critico else dano_base
                hp_jogador1 -= dano
                if critico:
                    print("dano dobrado!!")
                print(f"{jogador2} atacou {jogador1} e causou {dano} de dano!")
            else:
                cura = 20
                hp_jogador2 += cura
                print(f"{jogador2} se curou em {cura} HP!")
        else:
            print("[1] Atacar")
            print("[2] Curar")
            acao = input("Escolha : ")

            if acao == "1":
                critico = random.randint(1, 100) <= 10
                dano_base = max(1, atq_jogador2 - def_jogador1)
                dano = dano_base * 2 if critico else dano_base
                hp_jogador1 -= dano
                if critico:
                    print("dano dobrado!!")
                print(f"{jogador2} atacou {jogador1} e causou {dano} de dano!")
            elif acao == "2":
                cura = 20
                hp_jogador2 += cura
                print(f"{jogador2} se curou em {cura} HP!")

    turno += 1

if hp_jogador1 <= 0:
    print(f"\n{jogador2} ganhou!")
else:
    print(f"\n{jogador1} ganhou!")
