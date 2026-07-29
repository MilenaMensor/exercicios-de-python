''' =============EXERCICIO 07=========== '''
# INPUT pedindo para digitar uma palavra, tiro o espaco em branco com STRIP e transformo para MINUSCULO com LOWER
palavra = str(input('Digite uma palavra: ')).strip().lower()

# Utilizo o IF-ELSE para verificar se existe Z na palavra, uso o metodo IN
if 'z' in palavra:
    # Caso sim ele imprimi a seguinte frase:
    print('Tem Z! em sua palavra')
else:
    # Caso nao, ele imprimi a seguinte frase:
    print('Nao tem Z em sua palavra')


''' ===========EXERCICIO 08============ '''

# INPUT pedindo para digitar o nome completo, retiro os espacos sem sentido com STRIP e tranformo com UPPER para maiusculo
nome = str(input('Digite o seu nome completo: ')).strip().upper()

# Uso o format e mostro o NOME ja transformado com UPPER
print('\nSeu nome em letra maiuscula: {}'.format(nome))
# Uso o format para mostrar o nome e o TITLE para deixar apenas as primeiras letras de cada palavra em MAIUSCULO
print('Seu nome normal: {}'.format(nome.title()))

