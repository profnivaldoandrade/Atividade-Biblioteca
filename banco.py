import mysql.connector

class BancoDeDados:
    def __init__(self):
        try:
            self.conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password = "12345678",
                database = "DB_BIBLI"
            )
            self.cursor = self.conexao.cursor()
            print("Conexão BD ok")
        except mysql.connector.Error as err:
            print("Erro {err}")
        
        def inserir_livro(self, livro):
            try:
                sql = """"
                    INSERT INTO LIVRO(TITULO, AUTOR, ANO_PUBLI,L_STATUS)
                    VALUES(%s,%s,%s, %s)
                """
                valores =(livro.get_titulo(), livro.get_autor(), livro.get_ano_publicacao(), livro.get_status())
                self.cursor.execute(sql, valores)
                self.conexao.commit()
                print("Livro inserido com sucesso")
            except mysql.connector.Error as err:
                print("Erro: {err}")
        def consultar_livro(self, titulo):
            try:
                sql = "SELECT * FROM LIVROS WHERE TITULO = %s"
                self.cursor.execute(sql,(titulo,))
                resultado = self.cursor.fetchall()
                if resultado:
                    for livro in resultado:
                        print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Status: {livro[4]}")
                else:
                    print("Livro não Encontrado")
            except mysql.connector.Error as err:
                print("Erro: {err}")
