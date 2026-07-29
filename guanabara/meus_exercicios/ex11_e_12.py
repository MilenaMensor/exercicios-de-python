''' ===========EXERCICIO 11=========== '''

frase = str(input('Digite uma frase: ')).strip().lower()

print('Analisando a sua frase....')
print('Numero de caracteres(sem espacos): {}'.format(len(frase) - frase.count(' ')))
print('Quantidade de letras "a": {}'.format(frase.count('a')))
print('Contem a palavra "amor": {}'.format('amor' in frase))

''' =========EXERCICIO 12=========== '''

print('\nEXERCICIO 12')
frase2 = str(input('\nDigite um frase: ')).strip()

print('Essa e a sua frase: {}'.format(frase2.capitalize()))
print('Ela invertida entre maiusculo e minusculo: {}'.format(frase2.swapcase()))

