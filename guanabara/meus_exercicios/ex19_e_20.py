print('\nEXERCICIO 19 (MAIOR OU MENOR DE IDADE)')
print('=-' * 25)

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('Voce e MAIOR de idade! Parabens!\n')
else:
    print('Voce e MENOR de idade! Ja ja fica mais velho.\n')

print('EXERCICIO 20 (CONCEITO DA NOTA)')
print('=-' * 25)

nota = float(input('Digite a sua nota final(0 a 10): '))

if nota < 5:
    print('REPROVADO! Infelizmente voce repetiu de ano.')
elif nota > 5 and nota < 6.9:
    print('RECUPERACAO! Voce esta de recuperacao, pode refazer para recuperar a nota')
else:
    print('APROVADO! Parabens, voce foi aprovado, passou de ano.')
