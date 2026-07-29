print('=-' * 25)
print('EXERCICIO 29 (ACESSO AO SISTEMA 3)')

user = str(input('Insira o usuario: '))
senha = str(input('Insira a senha: '))

user1 = 'usuario'
senha1 = 'senha123@'
codigo1 = 'salsicha'

if user == user1 and senha == senha1:
    print('Acesso Liberado!')
    codigo = str(input('Digite o codigo de seguranca: '))
    
    if codigo == codigo1:
        print('Codigo Correto! Seja bem-vindo, aproveite o nosso sistema')
    else:
        print('Acesso Negado ao sistema! Codigo esta incorreto.')

elif user != user1 and senha == senha1:
    print('Acesso Negado! Usuario esta incorreto!')
    
elif user == user1 and senha != senha1:
    print('Acesso Negado! A senha esta incorreta!')
else:
    print('Acesso Negado! O usuario e senha estao incorretos!')

