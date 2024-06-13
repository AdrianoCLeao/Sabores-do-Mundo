# Sabores do Mundo

Sabores do Mundo é um projeto de site de receitas desenvolvido com Django, que permite aos usuários explorar receitas de várias culturas e adicionar suas próprias receitas. 

## Funcionalidades

- Navegação por categorias de receitas
- Pesquisa de receitas por nome ou ingrediente
- Detalhes de cada receita, incluindo ingredientes e instruções
- Sistema de registro e login de usuários
- Adição e gerenciamento de receitas pelos usuários registrados
- Comentários e avaliações das receitas

## Tecnologias Utilizadas

- Django: Framework web utilizado para o desenvolvimento do backend.
- SQLite: Banco de dados utilizado para armazenar as informações das receitas e dos usuários.
- HTML/CSS: Linguagens de marcação e estilo utilizadas para a construção do frontend.
- JavaScript: Linguagem de programação utilizada para adicionar interatividade ao site.

## Instalação

Para rodar este projeto localmente, siga os passos abaixo:

1. Clone o repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/seu-usuario/sabores-do-mundo.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd sabores-do-mundo
    ```

3. Crie um ambiente virtual:
    ```bash
    python -m venv env
    ```

4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        env\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source env/bin/activate
        ```

5. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

6. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
