print('\nEXERCICIO 17 (PODE VOTAR)')
print('=-' * 25)

idade = int(input('Digite a sua idade: '))

if idade >= 16:
    print('Voce JA PODE votar, va ate um local mais proximo para fazer o seu titulo.\n')
else:
    print('Voce ainda NAO PODE votar.\n')

print('=-' * 25)
print('EXERCICIO 18 (SENHA CORRETA)')

senha = 'python123'

user_senha = str(input('Digite a senha: '))

if user_senha == 'python123':
    print('Acesso Permitido! Seja bem-vinda Milena!')
else:
    print('Acesso negado! Senha incorreta!')
