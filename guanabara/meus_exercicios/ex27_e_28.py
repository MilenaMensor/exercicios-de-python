print('EXERCICIO 27 (CINEMA)')
print('=-' * 25)

idade = int(input('Informe a sua idade: '))
carteira_estudante = int(input('Possui carteira de estudante: \n[1] Sim\n[2] Nao\nOpcao:'))

if idade < 18 and carteira_estudante == 1:
    print('Idade: {} / Carteira Estudantil: Possui'.format(idade))
    print('Seu ingresso e MEIA-ENTRADA, valor atual: R$15.00')

elif idade >= 18 and carteira_estudante == 1:
    print('Idade: {} / Carteira Estudantil: Possui'.format(idade))
    print('Seu ingresso e MEIA-ENTRADA, valor atual: R$15.00')

else:
    print('Idade: {} / Carteira Estudantil: Nao Possui'.format(idade))
    print('Seu ingresso e INTEIRO, valor atual: R$30.00')


print('=-' * 25)
print('EXERCICIO 28 (APROVACAO ESCOLAR)')

nota = float(input('Digite a sua nota: '))
frequencia = int (input('Digite a frequencia na escola(em porcentagem): '))

if frequencia >= 75:
    if nota >= 7:
        print('Parabens! O aluno esta APROVADO!')
    else:
        print('O Aluno infelizmente esta REPROVADO PELA NOTA')
else:
    print('O aluno foi REPROVADO POR FALTA')

