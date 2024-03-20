'''5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;'''

string = "Target"

print(string[::-1])
#ou
lista = list(string)
listaInvertida = []

for i in range(len(lista)-1, -1, -1):
    listaInvertida.append(lista[i])

palavraInvertida = ''.join(listaInvertida)
print(palavraInvertida)