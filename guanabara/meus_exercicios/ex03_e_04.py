''' ==========EXERCICIO 03=========== '''

# Peco pelo INPUT uma frase ou palavra para transformar, utilizo STRIP para retirar os espacos sem sentido
texto = str(input('Digite uma frase ou palavra: ')).strip()

print('Analisando....')
# Pego o que foi obitido pelo INPUT e transformo com o UPPER, utilizando o FORMAT para formartar o PRINT (DEIXA A PALAVRA/FRASE EM MAIUSCULO)
print('A sua frase/palavra em MAIUSCULO: {}'.format(texto.upper())) 
# Pego o que foi obtido pelo INPUT  e transformo com LOWER, utilizando o FORMAT para formartar o PRINT (DEIXA A PALAVRA/FRASE EM MINUSCULO)
print('A sua frase/palavra em minusculo: {}'.format(texto.lower())) 

''' =========EXERCICIO 04=========== '''

# INPUT para pedir uma frase aleatoria, tiro os espacos sem sentido com STRIP e coloco em minuscula com LOWER
frase = str(input('Obs: Toda palavra "ruim", sera substituida por "bom"\nDigite uma frase bonita: ')).strip().lower()

# Utilizo um if-else para verificar se a frase obtida no INPUT tem a palavra "ruim", usado o metodo IN
if 'ruim' in frase :
    # Caso tenha 'ruim' ele ira substituir por 'bom' e formartar a frase nova com o TITLE
    frase_nova = frase.replace('ruim', 'bom')
    print('A sua frase foi substituida: {}'.format(frase_nova.title()))
else :
    # Caso nao tenha ele ira manter a frase obtida e imprimir ela normalmente
    print('A sua frase se manteve igual: {}'.format(frase.capitalize()))

