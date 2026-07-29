''' ===========EXERCICIO 01=========='''

#Peco pelo monitor para a pessoa escrever uma palavra pelo teclado, e logo em seguida retiro os espacos em branco com 
#o STRIP() e transformo toda a palavra com o UPPER()

palavra = str(input('Digite uma palavra: ')).strip().upper()

print('Analisando a palavra {}'.format(palavra)) # Print em uma pequena mensagem para ficar bonitinho
print('Quantidade de "A": {}'.format(palavra.count('A'))) # Print na informacao de A e utilizo o format para usar o COUNT() e mostrar quantos "A" tem na palavra
print('Tem "A" na sua palavra: {}'.format('A' in palavra))

''' ============EXERCICIO 02============= '''

# Peco pelo teclado para digitar uma frase, logo em seguida tiro os espacos inuteis
frase = str(input('Digite uma frase: ')).strip()

frase_caps = frase.upper() # Pego a frase e a transformo toda em maiuscula utilizando UPPER()

print('Analisando sua frase...')
# Uso o format para mostrar a frase normal
print('Sua frase e: {}'.format(frase))
# Uso format e logo em seguida o IN para procurar a palavra PYTHON na frase obtida pelo teclado
print('Existe a palavra "Python" em sua frase: {}'.format('PYTHON' in frase_caps))

