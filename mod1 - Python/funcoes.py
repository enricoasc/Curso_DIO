def exibir_mensagem():
    print('olá Mundo')

def exibir_mensagem2(nome):
    print(f'bem vindo {nome}')

def exibir_mensagem3(nome='alguem'):
    print(f'bem vindo {nome}')

exibir_mensagem()
exibir_mensagem2('enrico')
exibir_mensagem3('Enc')

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucesso(numero):
    antecessor = numero -1
    suscessor = numero + 1
    return antecessor,suscessor

print(calcular_total([5,9,6,7,8]))
print(retorna_antecessor_sucesso(25))

#argumentos nomeados 
def salvar_carro(marca, modelo, ano, placa):
    print(f'''Carro inserido com sucesso! 
          Marca: {marca}/ 
          Modelo: {modelo}/
          Ano: {ano}
          Placa: /{placa}''')

salvar_carro('Fiat','Palio', 1999, 'ABC-1234')
salvar_carro(modelo='Palio',marca='Fiat',placa='CBA-1234', ano=1999 )
salvar_carro(**{'marca':'Palio','modelo':'Fiat','ano':1999, 'placa':'QQQ-5432'})

# ARGS E KWARGS 
