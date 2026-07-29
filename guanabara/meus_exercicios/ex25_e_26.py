print('EXERCICIO 25 (EMPRESTIMO)')
print('-=' * 25)

salario = float(input('Digite o seu salario atual: R$'))
prestacao = float(input('Digite a prestacao: R$'))

minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Voce foi LIBERADO para o emprestimo')
else:
    print('Voce foi NEGADO para o emprestimo.')
    

print('=-' * 25)
print('EXERCICIO 26 (DESCONTO NA LOJA)')

valor = float(input('Digite o valor total da compra: '))

if valor >= 100:
    print('\nEscolha a forma de pagamento: ')
    escolha = int (input('''
[1] A vista
[2] Cartao Credito
'''))

    if escolha == 1:
        desconto = (valor * 10) / 100
        valor_final = valor - desconto
        print('VALOR TOTAL DA COMPRA: R${}'.format(valor))
        print('A sua compra teve desconto de 10%. Preco Atualizado: R${}'.format(valor_final))
    else:
        desconto = (valor * 5)/ 100
        valor_final = valor - desconto
        print('VALOR TOTAL DA COMPRA: R${}'.format(valor))
        print('A sua compra teve desconto de 5%. Preco Atualizado: R${}'.format(valor_final))
else:
    print('O valor da sua compra e de R${}'.format(valor))