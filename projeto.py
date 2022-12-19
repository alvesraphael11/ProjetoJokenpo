from time import sleep
from random import randint
vpc = 0
vjog = 0
emp = 0
r2 = 'S'
tot = 0
opcoes = ['nada', 'pedra', 'papel', 'tesoura']
print('-' * 30)
print('{:^30}'.format('JOKENPÔ'))
print('-' * 30)
while r2 == 'S':
  print('\nAs opções do jogo são: \n[ 1 ] Pedra \n[ 2 ] Papel \n[ 3 ] Tesoura')
  r = int(input('\nQual é o número da sua jogada? '))
  while r != 1 and r != 2 and r != 3:
    r =int(input('OPÇÃO INVÁLIDA! Você deve escolher entre as opções 1, 2 e 3: '))
  pc = randint(1, 3)
  sleep(1)
  print('\nOkay... preparado?')
  sleep(3)
  print('\nJO')
  sleep(1)
  print('KEN')
  sleep(1)
  print('PÔ!')
  sleep(1)
  print('\nEu escolhi {} e você escolheu {}...'.format(opcoes[pc], opcoes[r]))
  if r == 1 and pc == 1 or r == 2 and pc == 2 or r == 3 and pc == 3:
    print('Foi empate!')
    emp = emp + 1
  if r == 1 and pc == 2:
    print('Papel ganha de pedra. Eu ganhei!')
    vpc = vpc + 1
  if r == 1 and pc == 3:
    print('Tesoura perda para pedra. Você ganhou!')
    vjog = vjog + 1
  if r == 2 and pc == 3:
    print('Tesoura ganha de papel. Eu ganhei!')
    vpc = vpc + 1
  if pc == 1 and r == 2:
    print('Pedra perde para papel. Você ganhou!')
    vjog = vjog + 1
  if pc == 1 and r == 3:
    print('Pedra ganha de tesoura. Eu ganhei!')
    vpc = vpc + 1
  if pc == 2 and r == 3:
    print('Papel perde para tesoura. você ganhou!')
    vjog = vjog + 1
  tot = tot + 1
  sleep(3)
  r2 = str(input('\nVamos jogar mais uma vez? [S/N] ')).strip().upper()
print('\nCerto, então o score do nosso jogo ficou assim:\n')
sleep(4)
print('-' * 30)
print('{:^30}'.format('SCORE'))
print('-' * 30)
print('\n{:<25}{:>5}'.format('Total de partidas', tot))
print('{:<25}{:>5}'.format('Minhas vitórias', vpc))
print('{:<25}{:>5}'.format('Suas vitórias', vjog))
print('{:<25}{:>5}'.format('Total de empates', emp))
sleep(3)
print('\nFoi muito bom jogar com você. volte sempre! :D')