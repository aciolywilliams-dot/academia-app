import sqlite3

def conectar():
    return sqlite3.connect('academia.db')

def criar_tabela():
    conn = conectar()  # Abre a conexão com o banco de dados
    cursor = conn.cursor() # Cria um cursor para executar comandos SQL
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        data_nascimento TEXT NOT NULL,
        data_matricula TEXT NOT NULL,
        pagamento TEXT NOT NULL
    )
    """) 
    #Cria a tabela 'alunos' se ela não existir 
    # O .execute é usado para executar comandos SQL
    # Nesse caso, seleciona todos os registros da tabela 'alunos'

    conn.commit() # Salva as alterações no banco de dados
    conn.close() # Fecha a conexão com o banco de dados

def inserir_aluno(nome, cpf,nasc,matricula, pagamento):
    # Função para inserir um novo aluno na tabela 'alunos'
    conn = conectar() 
    cursor = conn.cursor() 
    cursor.execute("""
    INSERT INTO alunos (nome, cpf, data_nascimento, data_matricula, pagamento)
    VALUES (?, ?, ?, ?, ?)
    """, (nome, cpf, nasc, matricula, pagamento))
    # O ? são placeholders, para evitar erro de SQL Injection
    # Insere um novo aluno na tabela 'alunos'

    conn.commit() 
    conn.close() 

def listar_alunos():
    # Função para listar todos os alunos cadastrados na tabela 'alunos'
    conn = conectar() 
    cursor = conn.cursor() 

    cursor.execute("SELECT * FROM alunos") 
    alunos = cursor.fetchall() 
    # O .fetchall() retorna todos os registros da consulta como uma lista de tuplas
    conn.close() 
    return alunos # Retorna a lista de alunos para ser usada em outras partes do programa

def buscar_por_id(id):
    # Função para buscar um aluno pelo ID
    conn = conectar() 
    cursor = conn.cursor() 

    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id,)) 
    aluno = cursor.fetchone() 
    # O .fetchone() retorna o primeiro registro da consulta como uma tupla
    conn.close() 
    return aluno # Retorna o aluno encontrado ou None se não for encontrado

def atualizar_aluno(id, nome, cpf, nasc, matricula, pagamento):
    # Função para atualizar os dados de um aluno existente
    conn = conectar() 
    cursor = conn.cursor() 

    cursor.execute("""
    UPDATE alunos
    SET nome = ?, cpf = ?, data_nascimento = ?, data_matricula = ?, pagamento = ?
    WHERE id = ?
    """, (nome, cpf, nasc, matricula, pagamento, id))
    # Atualiza os dados do aluno com o ID especificado

    conn.commit() 
    conn.close()

def deletar_aluno(id):
    # Função para deletar um aluno pelo ID
    conn = conectar() 
    cursor = conn.cursor() 

    cursor.execute("DELETE FROM alunos WHERE id = ?", (id,)) 
    # Deleta o aluno com o ID especificado
    linhas = cursor.rowcount 
    # O .rowcount retorna o número de linhas afetadas pela última operação SQL

    conn.commit() 
    conn.close()

    return linhas # Retorna o número de linhas deletadas (0 ou 1) para indicar se a operação foi bem-sucedida

if __name__ == "__main__":
    criar_tabela()
    # Este bloco é executado apenas quando o script é executado diretamente
    # Ele chama a função criar_tabela para garantir que a tabela 'alunos' exista
    