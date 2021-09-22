# convierta la siguiente frase en un diccionario:
# words = "Biomédica:35-Medicina:14-Nutrición:22-Derecho:2"
words = "Biomédica:35-Medicina:14-Nutrición:22-Derecho:2"
dicc = dict((l.split(':') for l in words.split('-')))
print(dicc)