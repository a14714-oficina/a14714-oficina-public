#ex0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("insira a sua idade")
nome = input("insira o seu nome")
print(f"o meu nome é {nome} e tenho {idade} anos")
--------------------------------------------------------------
#ex0.2
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Ola, mundo!")
fruta ="Manga"
print(f"eu gosto de {fruta}");
---------------------------------------------------
#EX0.3
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input(" digite o seu nome")
print(f"ola {nome}, tudo bem")
valor = input("digite um numero inteiro :")
dobro =  valor * 2
print (f" o dobro de {valor} é {dobro}")
---------------------------------------------------------
#EX0.4
print("hello world")
nome = input("insira seu nome")
soma = (0-20)
nota = input("insira a sua nota")
media = soma/2;
if  media >10:
  print("aprovado")
if  media <10:
  print("carlos voce foi reprovado")
  -------------------------------------------------------
  print("hello world")
  #EX1.1
  """
  Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
  """
  a = "\n"
  print("\nBem-vindos ao Python!")

  #EX1.2
  """
  Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
  """
  print("\nJosé, bem-vindo ao python!")

  #EX1.3
  """
  Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
  """
  nome = "Carlos, bem-vindo ao python!")
  print (nome)
---------------------------------------------
#EX1.4
"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""
nome = input("\n insira o seu nome")
idade = input("\n insira a sua idade")
loc = input ( "\n insira a sua localidade")
-----------------------------------------------------
#EX1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem

"""
linguagem = "python"
nome = "carlos"
print(f"o {nome} sabe programar em {linguagem}")
-------------------------------------------------
#EX1.6
"""
Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""
print({f"bem vindo ao phyton!":<50})
print(f{"bem vindo ao phyton":^50})
print(f{"bem vindo ao phyton!":>50})
------------------------------------------------
#EX1.7
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""
raio = input("insira o raio")
perimetro = 2*3.14*raio
area = 3.14 * raio**2
print(f"o perimetro é {perimetro} e a area é {area}")
-------------------------------------------------
#EX1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
import datetime
x = datetime.datetime.now()
dia = x.strftime("%d")
mes = x.strftime("%m")
ano = x.strftime("%g")
horas = x.strftime("%H")
minutos = x.strftime("%M")
segundos = x.strftime("%S")
print(f"{dia}-{mes}-{ano} {horas}:{minutos}:{segundos}")
---------------------------------------------------------------------
#EX1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""
numero = input("insira o numero do atleta")
pontos = input("insira a pontuação final")
print(f"o atleta numero {numero} obteve {pontos} pontos")
----------------------------------------------------------------
#EX1.10
"""
Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual.
"""
import datetime
data = input("insira a sua data de nascimento")
dia = x.strftime("%d")
mes = x.strftime("%m")
ano = x.strftime("%g")
print(f"{dia} - {mes} - {ano}")
idade = 2024 - 2008
print(f"a sua idade é {idade}")
--------------------------------------------------------
#EX1.11
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO).
"""
libras = input("insira o valor em libras")
euros = 1,19 * libras
print(f"o valor em euros é {euros
--------------------------------------------
#autonomia
nome= str(input("qual o modelo gostas mais, alfa pendular ou metro do porto:"))
if nome == "alfa pendular":
  print("UAU, é mesmo rapido")
else:
  print("hmm, bom mas é lento")
  print("obrigado eu tambem gosto, {}!".format(nome))
  ---------------------------------------------------
  #DESAFIO 028
  import random

  segredo = int(random.randint(0, 5))
  # print(f"o numero secreto é {segredo}")

  numeroescolhido = int(input("insira um valor entre 0 e 5:"))

  if numeroescolhido > segredo:
    print("o numero escolhido é maior que o meu!")
  elif numeroescolhido < segredo:
    print("o numero escolhido é menor que o meu!")
  else:
    print("Acertaste!")
   ----------------------------------------------------------
   #FP1 
    """
    Exercício FP1: Verificar se um número é positivo, negativo ou zero.
    Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
    Dica: Usa as estruturas condicionais if, elif e else.
    """
    numero = int(input("insira um numero:"))
    if numero > 0:
      print(" o numero é positivo")
    elif numero < 0:
      print("o numero é negativo")
    else:
      print("o numero é zero")
-----------------------------------------------------------------
#FP2
"""
Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %.
"""
numero = int(input("insira um numero inteiro:"))
if numero % 2 ==0:
  print("o numero é par")
elif numero %1 == 0: 
  print("o numero é impar")
  -----------------------------------------------------
#FP3
"""
Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:
Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"
"""
nota = int(input("insira a nota final: "))
if nota<10:
  print("reprovado")
if nota >= 10 and nota < 14:
  print("suficiente")
if nota >= 15 and nota< 17:
  print("Bom")
if nota >=17:
  print("muito bom!")
  ----------------------------------------------------
  #FP4
  celsius = float(input("insira a temperatura em celsius"))
  fahrenheit = celsius * 9/5 + 32
  kelvin = celsius + 273.15
  print("a temperatura em fahrenheit:",{fahrenheit})
  print("a temperatura em kelvin:", {kelvin})
  print("opçao invalida")
--------------------------------------------------------
"""
Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.
"""
#FP5
salario = float(input("Insira o seu salário mensal: "))
if salario <=1000:
  print("isento de impostos")
elif salario >=1001 and salario< 2000:
  imposto = salario * 0.10
  salarioImposto = salario - imposto
  print(f"O seu salário mensal com o imposto de 10% é de: {salarioImposto}")
elif salario >= 2000: 
  imposto = salario * 0.20
  salarioImposto = salario - imposto
  print(f"O seu salário mensal com o imposto de 20% é de: {salarioImposto}")
-----------------------------------------------------------------
#EXFP6
"""
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
"""
for i in range(1,11):
  print(i)
  ------------------------------------------------------------
  #EXFP7
  """
  Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.
  """
  soma = 0
  i = 1
  while i <= 100:
    soma += i 
    i += 1
    print("a soma de 1 a 100 é:", soma)
    -----------------------------------------------
    #EXFP8
    """
    Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.
    """
    frase = str(input("insira uma frase:"))
    vogais = 0
    for letra in frase:
      if letra == "aeiou":
        vogais += 1
    print(f"a frase tem {vogais} vogais")
    -----------------------------------------------------------------
    #EXFP9
    """
    Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
    """
    for i in range(1,51):
      if i*5==0:
        print(i)
--------------------------------------------
num1 = input("insira o numero 1: ")
num2 = input("insira o numero 2: ")
num3 = input("insira o numero 3: ")
num4 = input("insira o numero 4: ")
num5 = input("insira o numero 5: ")
media = (int(num1) + int(num2) + int(num3) + int(num4) + int(num5))
print(f"a média desses numeros é: ,{media} ")
--------------------------------------
#EXFP10
"""
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.
"""
notas = []
for i in range(1,6):
  num= int(input("escreva um numero inteiro: "))
  notas.append(num)
print(notas)
valor1 = (notas[0])
valor2 = int(notas[1])
valor3 = int(notas[2])
valor4 = int(notas[3])
valor5 = int(notas[4])
total = (valor1 + valor2 + valor3 + valor4+ valor5)/5
print(f"a média é: {total}")
-------------------------------------------------------------
#EXFP11
"""
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.
"""
numero = int(input("insira um numero inteiro: "))
divisores = 0
for i in range (1, numero +1):
  if numero % i == 0:#verifica se o resultado da divisão é 0
    divisores +=1 #incrementa o contador de divisores
if divisores == 2:
  print("é um numero primo") 
else:
  print("não é um numero primo")

-------------------------------------------------------------------
#EXFP12
"""
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
"""
lista = []
for i in range(1,21):
  if i % 2 == 0:
    lista.append(i)
print(f"lista de numeros pares:{lista}")
------------------------------------------------------
#EXFP13
"""
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
"""
texto = input("insira uma palavra ou frase: ")
textoinv = texto [::2] #script para inverter o texto
print(textoinv) #printar o texto invertido
------------------------------------------------------------
numero = int(input("introduz um numero"))
for i in range (1,11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
