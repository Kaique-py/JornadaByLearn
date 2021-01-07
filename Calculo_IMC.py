# Calculando o IMC:
def num_quadrado(numero):
  quadrado = numero ** 2
  return quadrado

def imc(peso, altura):
  altura_quadrada = num_quadrado(altura)
  meu_imc = peso / altura_quadrada
  print(f'O imc é {meu_imc}')
  return meu_imc
meu_imc = imc(75, 1.63)