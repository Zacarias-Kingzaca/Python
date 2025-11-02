from os import system
from abc import ABC, abstractmethod
system("cls")
print()

class Personagem(ABC):
    def __init__(self, nome, vida, forca,):
        self._nome = nome
        self._vida = vida
        self._forca = forca
        

    @abstractmethod
    def Atacar(self, alvo):
        pass

    @abstractmethod
    def Defender(self, dano):
        pass

    def estar_vivo(self):
        return self._vida > 0
    
    def exibir_status(self):
        print(f"{self._nome} - Vida: {self._vida}")


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=120, forca=20)

    def Atacar(self, alvo):
        print(f"{self.get_nome()} Atacou com uma espada, e causou 20 de danos!")
        alvo.Defender(self._forca)

    def Defender(self, dano):
        dano_recebido = dano - 5 #reduz dado com armadura
        dano_recebido = max(dano_recebido, 0)
        self._vida -= dano_recebido
        print(f"O {self._nome} Defendeu! Vida restante: {self._vida}")


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 80, forca = 10)
        self._mana = 50
        self._poder_magico = 25

    def Atacar(self, alvo):
        if self._mana >= 10:
            print(f"{self._nome} Lança uma bola de fogo !")
            alvo.Defender(self._poder_magico)
            self._mana -= 10
        else:
            print(f"{self.get_nome()} está sem mana e não consegui atacar!")
            alvo.Defender(self._forca)

    def Defender(self, dano):
        self._vida -= dano 
        print(f"O {self._nome} Defendeu! Vida restante: {self._vida}")

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 100, forca = 30)
        self._mana = 50

    def Atacar(self, alvo):
        if self._mana >= 10:
            print(f"{self._nome} lançou a flexa!")
            alvo.Defender(self._forca)
        else:
            print(f"{self.get_nome()} está sem mana e não consegui atacar!")

    def Defender(self, dano):
        self._vida -= dano
        print(f"O {self._nome} Defendeu! Vida restante: {self._vida}")

personagens = []

guerreiro = Guerreiro("Arthur")
mago = Mago("Merlim")
arqueiro = Arqueiro("Legolas")

personagens.append(guerreiro)
personagens.append(mago)
personagens.append(arqueiro)

for p in personagens:
    print(f"{p.__class__.name_} - {p.nome}")

print("====INÍCIO DO JOGO====")

atacante = personagens[0]
defensor = personagens[1]

for turno in range(3):
    print(turno + 1)
    atacante.Atacar(defensor)
    defensor.Defender()
    print(f"{defensor.nome} tem {defensor.vida} de vida\n")
    # Trocar atacante e defensor
    atacante, defensor = defensor, atacante

print("Combate encerrado!")