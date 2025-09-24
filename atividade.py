#Questão 1

for numero in range(1, 11):
  print(numero)

#Questão 2

numero = 2
while numero < 50:
  numero += 2
  print(numero)

#Questão 3

numero = int(input("Digite um número: "))
for num in range(1,11):
  print(f"{numero} x {num} = {numero * num}")

#Questão 4

for num in range(1, 101):
  print(f"{numero} + {num} = {numero + num}")

#Questão 5

contador = 11

while contador != 0:
  contador -= 1
  print(contador)
  if contador == 0:
    print("FOGO!")
    break

#Questão 6

palavra = "programação"
for letra in palavra:
  print(letra)

#Questão 7

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f"Sua média é {media}")

#Questão 8

maior = None

for num in range(1, 11):
  numero = int(input("Digite um número: "))
  if maior is None or numero > maior:
    maior = numero
print(f"O maior número é {maior}")

#Questão 9

senha = 13405

tentativa = int(input("Digite a senha: "))
while tentativa != senha:
  print("Senha incorreta")
  tentativa = int(input("Digite a senha: "))
print("Senha correta")

#Questão 10

palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contador = 0

for letra in palavra:
  if letra in vogais:
    contador += 1

print(f"A palavra possui {contador} vogais")

#Questão 11

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
num4 = int(input("Digite o último número: "))
num5 = int(input("Digite o último número: "))

multiplicação = num1 * num2 * num3 * num4 * num5
print(f"A multiplicação dos números é {multiplicação}")

#Questão 12

numero = int(input("Digite um número: "))

if numero > 1:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"{numero} é um número primo")
    else:
        print(f"{numero} não é um número primo")
else:
    print(f"{numero} não é um número primo")

#Questão 13

for num in range(1, 21):
  quadrado = num ** 2
  print(f"O quadrado de {num} é {quadrado}")

#Questão 14

num = int(input("Digite um número: "))
fatorial = 1

for i in range(1, num + 1):
  fatorial *= i

print(f"O fatorial de {num} é {fatorial}")

#Questão 15

termo1 = 0
termo2 = 1

print("Sequência de Fibonacci (15 termos):")

for i in range(15):
    print(termo1, end=" ")
    proximo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo

#Questão 16

limite = int(input("Digite um número: "))

print(f"Números ímpares de 1 até {limite}:")
for i in range(1, limite + 1):
    if i % 2 != 0:
        print(i)

#Questão 17

import random

numero_secreto = random.randint(1, 20)

print("Tente adivinhar o número (entre 1 e 20)!")

palpite = 0
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número é maior!")
    elif palpite > numero_secreto:
        print("O número é menor!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")


#Questão 18

palavra = input("Digite uma palavra: ").lower()

palindromo = True

for i in range(len(palavra)):
    if palavra[i] != palavra[-(i+1)]:
        eh_palindromo = False
        break

if eh_palindromo:
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')


#Questão 19

print("Números entre 1 e 100 que são múltiplos de 3 e 5:")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#Questão 20

print("---Menu---")
print("1. Somar números")
print("2.Calcular média")
print("3. Sair")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma dos números é: {soma}")

elif opcao == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    media = (num1 + num2 + num3) / 3
    print(f"A média dos números é: {media}")

elif opcao == 3:
    print("Saindo do programa...")
    exit()
else:
    print("Opção inválida!")