standard_input = '1,2,3,4,5,6'

def analise_vendas(vendas):
    # Calcule o total de vendas
    total_vendas = sum(vendas)
    # Realize a média mensal
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # Converta a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

vendas = obter_entrada_vendas()

print(analise_vendas(vendas))

print('1,2,3,4,5')
print('1,2,3,4,5'.split(','))
print(list(map(int,'1,2,3,4,5'.split(','))))