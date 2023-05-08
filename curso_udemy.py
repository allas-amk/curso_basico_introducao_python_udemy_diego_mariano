# -*- coding:utf-8 -*-
import random
from functools import reduce

"""
nome = 'Allas'
sobreNome = 'Maycon'
nomeDeFamilia = 'Do Valle'

idade = '31'

profissao = 'Engenheiro Analista e Desenvolvedor de Software e Sistemas'

if sobreNome == 'Allas':
    print(nome)
else:
    print('Não é a mesma coisa')

print('--------------------')

lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0, "ola","biscoito","bolacha",9.99,True]

for i in lista1:
    print(i)

for i in lista2:
    print(i)

for i in lista3:
    print(i)

for i in range(10,20,2):
    print(i)

print('--------- String ---------')

# string

a = 'Django'
b = 'Flask'

concatenar = a + " " + b

tamanho = len(concatenar)
print(tamanho)
print('------')
print(a[0])
print(a[1])
print(a[2])
print(a[3])

print(concatenar[0:5])

print('-----------')

print(concatenar)
print(concatenar.lower())
print(concatenar.upper())
print(concatenar)

print('--------')

print(concatenar)
concatenar = concatenar.upper()
print(concatenar)

print('--------')

concatenar = a + " " + b + "\n"

print(concatenar)

print('------')

concatenar = a + " " + b + " "

print(concatenar.strip())

print('-----------')

minha_string = "o rato roeu a roupa do rei de Roma"

minha_string1 = minha_string.split("r")
print(minha_string1)

print('-----------')

busca = minha_string.find("rei")
print(busca)

busca = minha_string.find("rainha")
print(busca)

busca = minha_string.replace("rei", "rainha")
print(busca)

print('-----------')

def soma(x, y):
    #print(x+y)
    return x + y

s = soma(2, 3)
print(s)


def multiplicacao(x, y):
    return x * y

m = multiplicacao(3, 4)

print(multiplicacao(2, 4))

print(soma(s, m))

print('-----------')
"""

#print('Manipulando arquivos')

"""
modo    função
r       somente leitura
w       escrita (caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)
a       leitura e escrita (adiona o novo conteúdo ao fim do arquivo)
r+      leitura e escrita
w+      escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
a+      leitura e escrita (abre o arquivo para atualização)

lendo arquivos
read()
- lê arquivo inteiro
readline()
- lê uma linha
readlines()
- lê arquivo e o armazena em uma lista
"""

print('-----------')

#arquivo = open("meu_arquivo.txt")

#print(arquivo)

#linhas = arquivo.readlines()

#texto_completo = arquivo.read()
#print(texto_completo)

#w = open("meu_arquivo1.txt","w")
"""
w = open("meu_arquivo1.txt","a")

w.write("Esse é o meu arquivo\n")

w.close()
"""

"""
for linha in linhas:
    print(linhas)
"""

#print("Listas e dicionários")
"""
Listas
- Representam conjuntos de dados
- Pode ser:
    - Numérica: [1,2,3,4,5]
    - Strings: ["bola","sapato","chuva"]
"""

#minha_lista = ["abacaxi","melancia","abacate"]
#minha_lista1 = [1,2,3,4,5]
#minha_lista2 = ["abacaxi",2,9.89,True]

#minha_lista.append("limao")

#if 3 in minha_lista1:
#    print("3 esta na lista")
#for item in minha_lista:
#    print(item)

#del minha_lista[2:]
#print(minha_lista)

#minha_lista_3 = []

#minha_lista_3.append(57)
#print(minha_lista_3)

#lista = [234,55,66,7,22,8865,4343,23434,661,11,223,44]
#lista.sort()
#lista.sort(reverse=True)
#lista.reverse()
#lista = sorted(lista)
#print(lista)

#minha_lista.sort(reverse=True)

#print(minha_lista)

#print('---- Dicionarios -----')
"""
Dicionarios
- Dicionarios são listas de associações compostas por:
    - uma chave
    - um valor correspondente
        
        dicionario = {´CHAVE´:´valor´}
"""

#meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

#for i in meu_dicionario.items():
#for i in meu_dicionario.values():
#for i in meu_dicionario.keys():
#    print(i)
#for chave in meu_dicionario:
#    print(chave+"-"+meu_dicionario[chave])

#for chave in meu_dicionario.items():
#    print(chave)

#random.seed(1)
#lista = [2, 344, 55]
#numero = random.choice(lista)
#numero = random.randint(0, 10)
#print(numero)

# ---------------------------------------

#a = 2
#b = 0

#try:
#    print(a/b)
#except:
#    print("Não é permitida divisão por 0")

#print(a/a)

"""
Python 2 vs. Python 3
Python 2 vs. Python 3
Não muda muita coisa na prática. Python 3 possui melhor performance. Quanto a sintaxe, destaco apenas dois pontos:

1) Comando print( )
Ao executar o print, em Python 3, os parênteses passam a ser obrigatórios:

# Python 2
print "Olá mundo"
# Python 3
print("Olá mundo")


2) Comando input( )
Em Python 2 há duas variações do comando input:

raw_input( ) #strings
input( ) # valores numéricos
Em python 3, deve-se usar apenas input( ) para strings, e para números deve-se combinar com as funções float ou int. Veja:

# Recebendo textos
meu_texto = input("Digite um texto: ")
# Recebendo números
numero_inteiro = int(input("Digite um numero inteiro: "))
numero_decimal = float(input("Digite um numero decimal: "))


Atenção: a plataforma da Udemy e o Sublime Text não aceitam o comando input( ), e você receberá uma mensagem como "EOFError: EOF when reading a line". Esse comando só funciona no terminal/cmd. Para realizar os exercícios na Udemy, apenas insira o valor diretamente na variável.
"""

"""
Respostas dos exercícios
Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   

idade = int(input("Digite sua idade: "))
 
if idade >= 18:
    print("Maior de idade")
elif idade < 18:
    print("Menor de idade")


2. Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
 
media = (nota1+nota2)/2
 
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")


3. Escreva um programa que resolva uma equação de segundo grau.   

from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
 
if delta < 0:
    print("Delta negativo")
else:
    raiz_delta = sqrt(delta)
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
 
    print("As raízes são", x1, "e", x2)


4. Escreva um programa que ordene uma lista numérica com três elementos.   

lista = [3,2,1]
print(sorted(lista))


5. Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   

n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
n2 = int(input("Digite o segundo número: "))
 
if sinal == "+":
    op = n1 + n2
 
elif sinal == "-":
    op = n1 - n2
 
elif sinal == "/":
    op = n1 + n2
 
elif sinal == "*":
    op = n1 * n2
 
else:
    print("Sinal inválido.")
 
print(op)
"""


"""
Tópicos avançados em Python
A seguir serão apresentados alguns tópicos avançados em Python:
enumerate

list comprehension

map

reduce

zip

filter

Boas aulas.
"""

# list comprehension

#x = [1,2,3,4,5]
#y = []
#y = [i**2 for i in x]
#z = [i for i in x if i%2==1]

#for i in x:
#    y.append(i**2)

#print(z)
#print("Usando list comprehension")
#print(x)
#print(y)

# Função enumerate

#lista = ["abacate", "bola", "cachorro"]

#for i, nome in enumerate(lista):
#    print(i, nome)
#for i in range(len(lista)):
#    print(i, lista[i])

# map

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]
#print(dobro(valor))
#print(map(dobro, valor))

#valor_dobrado = map(dobro, valor)

#valor_dobrado = list(valor_dobrado)
#print(valor_dobrado)

#for v in valor_dobrado:
#    print(v)

# função reduce

#def soma(x, y):
#    return x+y

#lista = [1, 3, 5, 10, 20]

#soma = reduce(soma, lista)

#print(soma)

# zip

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$ 2,00", "R$ 5,00", "Não tem preço", "Não tem preço", "Não tem preço"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)