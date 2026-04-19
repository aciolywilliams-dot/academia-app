# 🔐 Segurança:
# O CPF é armazenado criptografado no banco de dados usando Fernet.
# Isso impede leitura direta dos dados sensíveis caso o banco seja acessado externamente.
# A descriptografia ocorre apenas na camada de leitura (listagem/busca).

import sqlite3
from utils.seguranca import criptografar, descriptografar

def conectar():
    return sqlite3.connect('academia.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()

def inserir_aluno(nome, cpf, nasc, matricula, pagamento):

    # Criptografa o CPF antes de salvar no banco

    cpf = criptografar(cpf)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO alunos (nome, cpf, data_nascimento, data_matricula, pagamento)
    VALUES (?, ?, ?, ?, ?)
    """, (nome, cpf, nasc, matricula, pagamento))

    conn.commit()
    conn.close()

def listar_alunos():

    # Busca todos os alunos

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()

    alunos_descriptografados = []

    for aluno in alunos:
        id_aluno, nome, cpf, nasc, matricula, pagamento = aluno
        cpf = descriptografar(cpf)

        # Descriptografa o CPF antes de mostrar na interface

        alunos_descriptografados.append(
            (id_aluno, nome, cpf, nasc, matricula, pagamento)
        )

    return alunos_descriptografados

def buscar_por_id(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id,))
    aluno = cursor.fetchone()
    conn.close()

    if aluno is None:
        return None

    id_aluno, nome, cpf, nasc, matricula, pagamento = aluno

    # Descriptografa o CPF antes de retornar
    
    cpf = descriptografar(cpf)

    return (id_aluno, nome, cpf, nasc, matricula, pagamento)

def atualizar_aluno(id, nome, cpf, nasc, matricula, pagamento):

    # Criptografa o CPF antes de atualizar no banco

    cpf = criptografar(cpf)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE alunos
    SET nome = ?, cpf = ?, data_nascimento = ?, data_matricula = ?, pagamento = ?
    WHERE id = ?
    """, (nome, cpf, nasc, matricula, pagamento, id))

    conn.commit()
    conn.close()

def deletar_aluno(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
    linhas = cursor.rowcount

    conn.commit()
    conn.close()

    return linhas

if __name__ == "__main__":
    criar_tabela()
    