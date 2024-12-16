import sqlite3
class Produto:
    def __init__(self,id_produto,nome, quantidade,preco):
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def _str_(self):
        return f"ID:{self.id_produto}, Nome:{self.nome}, Quantidade:{self.quantidade}, preco: R$ {self.preco:2f}"
    class ControleEstoque:
        def _init_(self, db_name = "estoque.db"):
            self.db_name = db_name
            self.conexao = sqlite3.connect(self.db_name) 
            self.cursor = self.conexao.cursor()
            self._criar_tabela()
        def _criar_tabela(self):
            self.cursor.execute ("""
            CREATE TABLE IF NOT EXISTS produto (
                                                id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                                                nome TEXT NOT NULL,
                                                quantidade INTEGER NOT NULL                                         
            );
            """)  
            self.conexao.commit()  
        def adicionar_produto(self, nome, quantidade, preco):
            self.cursor.execute(" INSERT INTO produto(nome,quantidade,preco)VALUES (???)",(nome,quantidade,preco))
            self.conexao.commit()
        def listar_produto(self):
            self.cursor.execute("SELECT* FROM produto")
            produto = self.cursor.fetchall()
            return [Produto(id_produto, nome, quantidade, preco) for id_produto, nome, quantidade,preco in produto]
        def atualizar_quantidade(self, id_produto,quantidade):
            self.cursor.execute("UPDATE produto SET quantidade = ? WHERE id_produto = ?",(quantidade, id_produto))
            self.conexao.commit()
        def remover_produto(self, id_produto):
            self.cursor.execute("DELETE FROM produto WHERE id_produto = ?",(id_produto,))
            self.conexao.commit()

            
                                

        

            


