''' ===========EXERCICIO 09=========== '''

frase = str(input('Digite uma frase com muitos espacos em branco sem sentido: '))

print('\nAqui esta sua frase: {}'.format(frase))
print('Agora essa e a sua frase escrita corretamente:\n{}'.format(frase.strip(' ')))

''' =========EXERCICIO 10============ '''

frase = str(input('Digite um frase: ')).strip().lower()

frase_subs = frase.replace('a', '@', 1)

print('A sua frase original: {}'.format(frase.capitalize()))
print('A sua frase com a substituicao: {}'.format(frase_subs.capitalize()))

