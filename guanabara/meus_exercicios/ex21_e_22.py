print('EXERCICIO 21 (CALCULADORA)')
print('-=' * 25)

num1 = float(input('\nDigite o PRIMEIRO NUMERO: '))
num2 = float(input('Digite o SEGUNDO NUMERO: '))

print('''\nESCOLHA A OPERACAO:
         [1] Soma
         [2] Subtracao
         [3] Multiplicacao
         [4] Divisao''')
escolha = int(input('Operacao: '))

if escolha == 1:
    print('\nOPERACAO ESCOLHIDA: SOMA')
    print('{} + {} = {}'.format(num1, num2, num1+num2))
elif escolha == 2:
    print('\nOPERACAO ESCOLHIDA: SUBTRACAO')
    print('{} - {} = {}'.format(num1, num2, num1-num2))
elif escolha == 3:
    print('OPERACAO ESCOLHIDA: MULTIPLICACAO')
    print('{} * {} = {}'.format(num1, num2, num1*num2))
elif escolha == 4:
    print('OPERACAO ESCOLHIDA: DIVISAO')
    print('{} / {} = {}'.format(num1, num2, num1/num2))
else:
    print('Escolha nao encontrada ou incorreta, por favor tente novamente.')

print(' ')
print('-=' * 25)
print('EXERCICIO 22 (FAIXA ETARIA)')

idade = int(input('Insira a sua idade: '))

if idade > 0 and idade <= 12:
    print('Voce e uma: CRIANCA')
elif idade >= 13 and idade <= 17:
    print('Voce e um: ADOLESCENTE')
elif idade >= 18 and idade <= 59:
    print('Voce e um: ADULTO')
else:
    print('Voce e um: IDOSO')
