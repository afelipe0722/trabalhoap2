from os import path

if path.exists("arquivo.txt"):
    arquivo = open('arquivo.txt', 'a+')
else:
    arquivo = open('arquivo.txt', 'w+')

while True:
    nome = str(input('Nome: '))
    telefone = str(input('Telefone: '))
    arquivo.write(f' nome:{nome} e telefone:{telefone}\n')
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
resp1 = str(input('Quer ver os usuários cadastrados? [S/N] ')).upper()[0]
if resp1 == 'S':
    arquivo = open('arquivo.txt', 'r')
    print(arquivo.read())
