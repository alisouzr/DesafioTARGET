'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''


numero = int(input('Informe um número: '))
primeiro = 0
segundo = 1
proximo = 0
sequencia = []

while proximo < numero:
  proximo = primeiro + segundo
  sequencia.append(proximo)
  primeiro = segundo
  segundo = proximo

if numero in sequencia:
    print('O número informado pertence a sequência de Fibonacci.')
else:
    print('O número informado não pertence a sequência de Fibonacci.')
