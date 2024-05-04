# TAREFA 1

def imprimir_informacoes(nome, idade, cidade):
  print(f'Nome: {nome}', f'idade: {idade}', f'Cidade: {cidade}', end="!", sep=" - ")

imprimir_informacoes("Ellen", "19", "São Gonçalo") 

# TAREFA 2

def calculos(a, b, operacao):
  if operacao == "+":
    print(a+b)
  elif operacao == "-":
    print(a-b)
  elif operacao == "*":
    print(a*b)
  elif operacao == "/":
    print(a/b)
  else:
    print("operação não encontrada")
    
calculos(1,2, "%")

# TAREFA 3

def lista_de_compras():
  print("Digite uma lista de compras separadas por vírgula\n")
  lista_em_str = input("Digite sua lista de compras: ")
  lista = lista_em_str.split(',')
  
  for item in range(len(lista)):
    print(f'Item {item + 1}: {lista[item]}')

lista_de_compras()

# TAREFA 4

def conversao():
  C = int(input('Digite o celsius: '))
  F = (C * 9/5) + 32
  print(f'Fahrenheit: {F}')     

conversao()

# TAREFA 5

def nomes():
  lista_de_nome = []
  nome = ''
  
  while nome != 'sair':
    nome = input('Digite o nome: ')
    lista_de_nome.append(nome)

nomes()
