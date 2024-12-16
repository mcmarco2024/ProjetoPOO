from Models.EstoqueModel import ControleEstoque
from Models.ProdutosModel import Produtos

estoque = ControleEstoque('estoque.db')


def Add_produto():
    nome = input("Nome: ")
    quantidade = input("Quantidade: ")
    valor = input("Valor: ")

    newProduto = Produtos()
    newProduto.set_prod(nome, quantidade, valor)

    if estoque.Add_Produto(newProduto.get_id(), newProduto.get_nome(), newProduto.get_quantidade(), newProduto.get_preco):
        print("Produto adicionado", newProduto.get_nome())
    else:
        print('Erro ao adicionar produto')
                