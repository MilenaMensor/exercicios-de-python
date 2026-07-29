''' ==========EXERCICIO 13=========== '''

frase1 = str(input('Digite uma frase: ')).strip()

print('Sua frase comeca com "Ola"? {}'.format(frase1.startswith('Ola')))
print('Sua frase termina com "!"? {}'.format(frase1.endswith('!')))

''' ==========EXERCICIO 14=========== '''
print('\nEXERCICIO 14')
frase2 = str(input('Digite uma frase: ')).strip().lower()

if 'feio' in frase2 or 'feia' in frase2:
    frase_subs = frase2.replace('feio', '****')
    frase_subs = frase2.replace('feia', '****')
    print('Sua frase contem "feio" ou "feia", ela foi censurada: \n{}'.format(frase_subs.capitalize()))
else: 
    print('Sua frase nao contem "feio" ou "feia", ela continua normal: \n{}'.format(frase2.capitalize()))
