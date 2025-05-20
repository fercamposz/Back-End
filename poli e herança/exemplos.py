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
