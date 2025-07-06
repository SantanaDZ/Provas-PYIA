class Animal:
    def falar(self):
        print("Este animal faz um som genérico.")


class Cachorro:
    def falar(self):
        print("O cachorro está latindo.")


class Gato:
    def falar(self):
        print("O gato está miando.")


# Criando objetos e chamando o método falar()
animal = Animal()
animal.falar()

cachorro = Cachorro()
cachorro.falar()

gato = Gato()
gato.falar()