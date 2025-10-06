from db import conectar

def criar_aluno(nome, idade):
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome, idade) VALUES (%s, %s)",
                (nome, idade)
            )
            conexao.commit()
        except Exception as  erro:
            print(f"erro ao criar aluno: {erro}")
        finally:
            cursor.close
            conexao.close()
    
def listar_alunos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM aluno ORDER BY id")
            return cursor.fetchall()
        except Exception as erro:
            print(f"erro ao tentar listar alunos:{erro}")
        finally:
            cursor.close()
            cursor.close()

lista = listar_alunos()
print(lista)
for aluno in lista:
    print(aluno)