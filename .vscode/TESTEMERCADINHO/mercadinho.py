class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Mercadinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        if any(p.id == produto.id for p in self.produtos):
            return False
        self.produtos.append(produto)
        return True

    def buscar_produto(self, id):

        return next((p for p in self.produtos if p.id == id), None)

    def atualizar_produto(self, id, novos_dados):
        produto = self.buscar_produto(id)
        if not produto:
            return False  
        produto.nome = novos_dados.get("nome", produto.nome)
        produto.preco = novos_dados.get("preco", produto.preco)
        produto.quantidade = novos_dados.get("quantidade", produto.quantidade)
        return True

    def remover_produto(self, id):
        tamanho_inicial = len(self.produtos)
        self.produtos = [p for p in self.produtos if p.id != id]
        return len(self.produtos) < tamanho_inicial

    def listar_produtos(self):
        return self.produtos

    def limpar(self):
        self.produtos = []


if __name__ == "__main__":
    mercado = Mercadinho()


    p1 = Produto(1, "Arroz", 10.50, 5)
    p2 = Produto(2, "Feijão", 8.99, 3)
    assert mercado.adicionar_produto(p1)
    assert mercado.adicionar_produto(p2)

   
    encontrado = mercado.buscar_produto(1)
    assert encontrado is not None
    assert encontrado.nome == "Arroz"


    assert mercado.buscar_produto(999) is None

   
    assert mercado.atualizar_produto(1, {"nome": "Arroz Integral"})
    assert mercado.buscar_produto(1).nome == "Arroz Integral"
    assert mercado.buscar_produto(1).preco == 10.50

 
    assert mercado.atualizar_produto(1, {"preco": 12.0})
    assert mercado.buscar_produto(1).preco == 12.0

    assert mercado.atualizar_produto(1, {"quantidade": 7})
    assert mercado.buscar_produto(1).quantidade == 7

    assert mercado.atualizar_produto(999, {"nome": "Não Existe"}) is False

 
    lista = mercado.listar_produtos()
    assert len(lista) == 2
    assert lista[0].nome == "Arroz Integral"
    assert lista[1].nome == "Feijão"

    assert mercado.remover_produto(2) is True
    assert mercado.buscar_produto(2) is None
    assert len(mercado.listar_produtos()) == 1


    lista_antes = mercado.listar_produtos().copy()
    assert mercado.remover_produto(999) is False
    assert mercado.listar_produtos() == lista_antes  


   
    mercado.limpar()
    assert mercado.listar_produtos() == []

    print("✅ Todos os testes passaram com sucesso!")
