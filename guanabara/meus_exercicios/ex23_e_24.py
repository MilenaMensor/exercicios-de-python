print('EXERCICIO 23 (TEMPERATURA)')
print('-=' * 25)

temp = float(input('\nQual a temperatura atual: '))

if temp < 15:
    print('A temperatura {} e de FRIO'.format(temp))
elif temp > 15 and temp < 29:
    print('A temperatura {} e de AGRADAVEL'.format(temp))
else:
    print('A temperatura {} e de QUENTE'.format(temp))    


print(' ')
print('EXERCICIO 24 (LOGIN)')
print('-=' * 25)

user = str(input('Digite o seu usuario: '))
senha = str(input('Digite a sua senha:'))

if user == 'admin' and senha == 'adm1234':
    print('\nLogin realizado com sucesso!\nSeja bem-vindo ADMIN')
else:
    print('\nUsuario ou senha incorretos! Por favor tente novamente.')

