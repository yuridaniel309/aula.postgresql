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
    
 
def atualiza_idade(id_aluno, nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE alunos SET idade = %s WHERE id = %s",
                (nova_idade, id_aluno)
                )
            conexao.commit()
        except Exception as erro: 
            print(f"erro ao tentar atualizar a idade {erro}")
        finally:
            cursor.close()
            conexao.close()

