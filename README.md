# Gerenciador de Tarefas

Este é um aplicativo web simples de gerenciamento de tarefas desenvolvido com **Django**, um framework Python, e **HTML/CSS** para a interface do usuário. O objetivo do projeto é permitir aos usuários criarem, visualizarem, editarem e excluírem tarefas.

Foi meu primeiro projeto após o tutorial oficial do **Django** (https://docs.djangoproject.com/pt-br/5.1/intro/tutorial01/). Desenvolver esse projeto foi desafiador e divertido, pois tive a oportunidade de colocar em prática os conhecimentos adquiridos no tutorial, além de aprender novos conceitos para implementar as funcionalidades que eu me propus a criar.

## Funcionalidades

- **Cadastro e Edição de Tarefas:** Crie novas tarefas e edite tarefas existentes com títulos, descrições e status.
- **Status de Tarefa:** As tarefas podem ser marcadas como "Pendente", "Em Andamento" ou "Concluída".
- **Validação de Data:** A data de conclusão não pode ser uma data futura, garantindo que os registros sejam consistentes.
- **Feedback Visual:** Mensagens de erro são apresentadas de forma clara ao usuário, sem sobrecarregar a interface.

## Tecnologias Utilizadas

- **Django 4.2** - Framework Python utilizado para o backend.
- **SQLite** - Banco de dados simples para armazenamento de dados.
- **HTML5 & CSS3** - Para a criação da interface do usuário.

## Como Rodar o Projeto Localmente

1. **Clonar o repositório:**
   ```bash main
   git clone https://github.com/GabrielSantos99/django_to_do_list#

2. **Configurar o banco de dados:**
    python manage.py migrate

3. **Rodar o servidor:**
    python manage.py runserver

4. **Acessar o aplicativo:**
    Abra o navegador e vá para http://127.0.0.1:8000 para acessar o aplicativo.