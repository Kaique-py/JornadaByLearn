# Calculando o IMC:
peso = float(input('Insira o peso: '))
altura = float(input('Insira a altura: '))
def num_quadrado(numero):
  quadrado = numero ** 2
  return quadrado

def imc(peso, altura):
  altura_quadrada = num_quadrado(altura)
  meu_imc = peso / altura_quadrada
  print(f'O imc é {meu_imc}')
  return meu_imc
meu_imc = imc(peso, altura)
