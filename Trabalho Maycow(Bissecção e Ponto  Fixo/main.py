from bissecao import *
from ponto_fixo import *

opcao = int(input('Qual método que deseja utilizar:\n1 - Bisseção\n2 - Ponto Fixo\n: '))

while opcao != 1 and opcao != 2:
    print('Opção inválida!')
    opcao = int(input('Qual método que deseja utilizar:\n1 - Bisseção\n2 - Ponto Fixo\n: '))

if opcao == 1:

    bissecao()

elif opcao == 2:

    ponto_fixo()
