''' =======EXERCICIO 05========'''\

# INPUT pedindo uma frase aleatorio, tiro os espacos em branco com STRIP e coloco a frase em MINUSCULO para facilitar com os comandos
frase = str(input('Digite uma frase: ')).strip().lower()

print('\nAnalisando a frase....\nObs: Os espacos em branco sao contados')
# procura pela primeira letra E na frase, soma com mais para aparecer corretamente no painel
print('\nO primeiro "e" da frase aparece na posicao: {}'.format(frase.find('e')+1))
# procura pela ultima letra E na frase, indo da direita pra esquerda, tambem soma com mais um
print('O ultimo "e" da frase aparece na posicao: {}'.format(frase.rfind('e')+1))

''' =======EXERCICIO 06========'''

# INPUT pedindo para digitar uma frase, tiro os espacos em brancos com STRIP e transformo toda em MINUSCULA com LOWER
frase = str(input('Digite uma frase: ')).strip().lower()

print('\nProcurando quantos "de" tem em sua frase...')
# Verifica quantos 'de' tem na frase utilizando o COUNT e depois o FORMAT para deixar arrumado
print('Foi/Foram encontrado(s): {}'.format(frase.count('de')))

