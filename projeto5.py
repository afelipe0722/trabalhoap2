class Pessoa:

    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def imc(self):
        return self.peso/(self.altura * self.altura)


nome = str(input('nome: '))
altura = float(input('altura: '))
peso = float(input('peso: '))
idade = int(input('idade: '))

pessoa=Pessoa(nome,idade,altura,peso)
print(f'imc={pessoa.imc()}')




