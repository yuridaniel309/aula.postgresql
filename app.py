import streamlit as st
from crud import criar_aluno, listar_alunos, atualiza_idade, deletar_aluno

st.set_page_config(page_title = "gerenciamento de alunos", page_icon="👨‍🎓")

st.title("sistema de alunos com postgresql")

menu = st.sidebar.radio("menu",["inserir","listar","atualizar","idade"])

if menu == "inserir":
    st.subheader("+ inserir alunos")
    nome = st.text_input("nome", placeholder= " seu nome")
    idade = st.number_input ("idade",min_value = 16,step = 1)
    if st.button("cadastrar"):
        if nome.strip() !="":
            criar_aluno(nome, idade)
            st.success(f"aluno {nome} inserindo com sucesso!")
        else:
            st.warning("o campo nome nao pode ser vazio.")

elif menu == "listar":
    st.subheader("listar_alunos")
    if alunos:
        # for linha in alunos:
        #     st.write(f"id ={linha[0]} | NOME = [linha[1]} |IDADE = linha[2]}")
else:
    st.info("nenhum aluno encontrado")