class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # TODOS: Implementar o método adicionar_venda para adicionar uma venda à lista de vendas:
    def adicionar_venda(self,vendas):
      self.vendas.append(vendas)
      
    # TODOS: Implementar o método total_vendas para calcular e retornar o total das vendas
    def total_vendas(self):
      total = 0
      for venda in self.vendas:
        total += venda.quantidade*venda.valor  
    
      return f'Vendas em {self.nome}: {total:.1f}'

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # TODOS: Adicione a venda à categoria usando o método adicionar_venda:
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
      categoria.total_vendas()
        # TODOS: Exibir o total de vendas usando o método total_vendas:

if __name__ == "__main__":
    main()