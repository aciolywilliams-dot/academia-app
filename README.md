# Sistema de Gerenciamento de Academia

Sistema desenvolvido em Python com PyQt6 para gerenciamento de alunos de uma academia, utilizando operações CRUD e versionamento com Git.

## Funcionalidades

- Cadastro de alunos
- Listagem com filtro de busca
- Atualização de dados
- Remoção de alunos com confirmação
- Validação de CPF
- Interface gráfica com tema claro/escuro

## Tecnologias utilizadas

- Python
- PyQt6
- SQLite
- Git e GitHub

## Como executar

1. Clone o repositório:
git clone https://github.com/aciolywilliams-dot/academia-app.git

2. Acesse a pasta do projeto:
cd academia-app

3. Instale as dependências:
pip install pyqt6

4. Inicialize o banco de dados (criação da tabela):
python banco.py

5. Execute o sistema:
python main.py

## Observações

- O arquivo do banco de dados (`academia.db`) é criado automaticamente ao executar o arquivo `banco.py`.
- Caso o banco não seja inicializado, o sistema pode apresentar erros ao tentar cadastrar ou listar alunos.

## Estrutura do projeto

- ui/ → telas do sistema
- utils/ → funções auxiliares (tema, validações)
- banco.py → operações e criação do banco de dados
- main.py → inicialização da aplicação

## Autor

Projeto desenvolvido para fins acadêmicos.