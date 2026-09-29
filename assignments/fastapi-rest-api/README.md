# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando FastAPI e modelos Pydantic. Você vai praticar rotas HTTP, validação de dados, códigos de status e documentação interativa.

## 📝 Tasks

### 🛠️ Criar endpoints de leitura

#### Descrição
Partindo do arquivo `starter-code.py`, implemente endpoints para listar tarefas e consultar uma tarefa pelo ID. Instale FastAPI e Uvicorn com `python -m pip install fastapi uvicorn` e inicie a aplicação com `uvicorn starter-code:app --reload`.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` para retornar a lista de tarefas
- Implementar `GET /tasks/{task_id}` para retornar a tarefa correspondente
- Retornar status `404` quando o ID solicitado não existir
- Permitir conferir os endpoints em `http://127.0.0.1:8000/docs`

### 🛠️ Adicionar criação e atualização

#### Descrição
Permita que clientes criem tarefas e atualizem tarefas existentes. Use os modelos Pydantic fornecidos para validar os dados recebidos no corpo das requisições.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` e atribuir um ID único à nova tarefa
- Retornar status `201` ao criar uma tarefa
- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão
- Retornar status `404` se a tarefa a atualizar não existir
- Deixar o FastAPI rejeitar dados inválidos com uma resposta de validação

### 🛠️ Implementar exclusão e verificar a API

#### Descrição
Complete as operações da API implementando a exclusão de tarefas. Use a interface `/docs` para enviar requisições e verificar os resultados de todos os endpoints.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /tasks/{task_id}` e remover a tarefa correspondente
- Retornar status `404` se a tarefa a excluir não existir
- Confirmar que a tarefa removida deixa de aparecer em `GET /tasks`
- Testar pelo menos uma criação, uma atualização e uma exclusão pela interface `/docs`