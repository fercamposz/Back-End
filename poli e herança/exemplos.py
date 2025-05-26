#poli
class pessoas:
    def __init__ (self, nomes):
        self.nomes = nomes
    def oi (self):
        print(f"Bom dia, sou uma pessoa e meu nome é: {self.nomes} ")
class Aluna(pessoas):
    def oi(self):
        print(f"Bom dia, sou aluna e meu nome é: {self.nomes}")

class Professor(pessoas):
    def oi(self):
        print(f"Bom dia, sou professor e meu nome é: {self.nomes}")


marcia = pessoas("Marcia")
marcia.oi()

fer = Aluna("Fernanda")
fer.oi()

dorival = Professor("Dorivas")
dorival.oi()

#herança
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")

class Aluna(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

class Professor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
marcia = Pessoa("Marcia")
marcia.apresentar()

fernanda = Aluna("Fernanda")
fernanda.apresentar()

dorival = Professor("Dorival")
dorival.apresentar()
