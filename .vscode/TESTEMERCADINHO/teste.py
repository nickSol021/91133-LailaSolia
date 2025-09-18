"""
Título: TESTE MERCADINHO PYTHON
Autor: LAILA NICHOLE DE MEDEIROS SOLIA
Data: 18/09/2025
"""

import unittest

# Código das classes Produto e Mercadinho (copiado do código fornecido)
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


class TestMercadinho(unittest.TestCase):

    def setUp(self):

        self.mercado = Mercadinho()

    def test_cadastro_produto_valido(self):
       

        produto = Produto(id=1, nome="Arroz", preco=10.50, quantidade=5)
        resultado = self.mercado.adicionar_produto(produto)
        self.assertTrue(resultado, "O método adicionar_produto deve retornar True para ID único.")
        self.assertIn(produto, self.mercado.listar_produtos(), "A lista de produtos deve conter o produto cadastrado.")

 
def test_cadastro_produto_id_duplicado(self):
    # Criando dois produtos com o mesmo ID
    produto1 = Produto(id=1, nome="Arroz", preco=10.50, quantidade=5)
    produto2 = Produto(id=1, nome="Feijão", preco=7.30, quantidade=3)
    
    # Adiciona o primeiro produto
    self.mercado.adicionar_produto(produto1)
    
    # Tenta adicionar o segundo produto com o mesmo ID
    resultado = self.mercado.adicionar_produto(produto2)
    
    # Verifica que a operação falhou devido ao ID duplicado
    self.assertFalse(resultado, "O método adicionar_produto deve retornar False para ID duplicado.")
    
    # Verifica que a lista de produtos ainda tem apenas um item
    self.assertEqual(len(self.mercado.listar_produtos()), 1, "Deve haver apenas um produto na lista.")

    def test_buscar_produto_existente(self):
        
        produto = Produto(id=2, nome="Açúcar", preco=4.20, quantidade=10)
        self.mercado.adicionar_produto(produto)
        buscado = self.mercado.buscar_produto(2)
        self.assertIsNotNone(buscado, "O produto deve ser encontrado.")
        self.assertEqual(buscado.nome, "Açúcar")

    def test_buscar_produto_inexistente(self):
      
        buscado = self.mercado.buscar_produto(999)
        self.assertIsNone(buscado, "Deve retornar None para produto inexistente.")

    def test_atualizar_produto_existente(self):
 
        produto = Produto(id=3, nome="Café", preco=15.00, quantidade=8)
        self.mercado.adicionar_produto(produto)
        novos_dados = {"nome": "Café Premium", "preco": 18.00, "quantidade": 10}
        resultado = self.mercado.atualizar_produto(3, novos_dados)
        self.assertTrue(resultado, "A atualização deve retornar True para produto existente.")
        atualizado = self.mercado.buscar_produto(3)
        self.assertEqual(atualizado.nome, "Café Premium")
        self.assertEqual(atualizado.preco, 18.00)
        self.assertEqual(atualizado.quantidade, 10)

    def test_atualizar_produto_inexistente(self):
      
        resultado = self.mercado.atualizar_produto(999, {"nome": "Produto X"})
        self.assertFalse(resultado, "A atualização deve retornar False para produto inexistente.")

    def test_remover_produto_existente(self):
       
        produto = Produto(id=4, nome="Leite", preco=3.50, quantidade=20)
        self.mercado.adicionar_produto(produto)
        resultado = self.mercado.remover_produto(4)
        self.assertTrue(resultado, "A remoção deve retornar True para produto existente.")
        self.assertIsNone(self.mercado.buscar_produto(4), "O produto deve ser removido da lista.")

    def test_remover_produto_inexistente(self):
     
        resultado = self.mercado.remover_produto(999)
        self.assertFalse(resultado, "A remoção deve retornar False para produto inexistente.")

    def test_listar_produtos(self):
       
        p1 = Produto(id=5, nome="Pão", preco=2.00, quantidade=15)
        p2 = Produto(id=6, nome="Manteiga", preco=5.00, quantidade=7)
        self.mercado.adicionar_produto(p1)
        self.mercado.adicionar_produto(p2)
        lista = self.mercado.listar_produtos()
        self.assertIn(p1, lista)
        self.assertIn(p2, lista)
        self.assertEqual(len(lista), 2)

    def test_limpar(self):
       
        p1 = Produto(id=7, nome="Queijo", preco=12.00, quantidade=4)
        self.mercado.adicionar_produto(p1)
        self.mercado.limpar()
        self.assertEqual(len(self.mercado.listar_produtos()), 0, "A lista deve estar vazia após limpar.")

if __name__ == "__main__":
    unittest.main()