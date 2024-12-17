# ERP System

Esta é a criação de um Sistema de Gestão Empresarial completo utilizando tecnologias de última geração: ReactJS e Django Rest Framework.

## ⛏️ Instalação

Execute o projeto com Python
    
    py manage.py runserver

## 💎 Stacks utilizadas

Front-end: ReactJS, TypeScript, React-Router, Redux, Material UI, Axios

Back-end: Django, Django Rest Framework, Simple JWT

## 📋 Documentação da API - Authentication
Autenticação - Criar Uma Conta
    
    POST /api/v1/auth/signup

| Parâmetro	| Tipo   |	Descrição   |
|-----------|--------|--------------|
| name      |	string |	Obrigatório |
| email     |	string |	Obrigatório |
| password  |	string |	Obrigatório |

Autenticação - Fazer Login

    POST /api/v1/auth/signin

| Parâmetro |	Tipo	  | Descrição   |
|-----------|---------|-------------|
| email     |	string	| Obrigatório |
| password	| string	| Obrigatório |

Autenticação - Obter Um Usuário - (Necessário Autenticação)

    GET /api/v1/auth/user

| Parâmetro     |	Tipo	  | Descrição                 |
|---------------|---------|---------------------------|
| Authorization	| string	| Obrigatório. Access Token |

## 📋 Documentação da API - Companies - Employees
Funcionários - Listar Funcionários De Uma Empresa - (Necessário Autenticação)

    GET /api/v1/companies/employees

Funcionários - Criar Um Funcionário - (Necessário Autenticação)

    POST /api/v1/companies/employees

| Parâmetro	| Tipo	  | Descrição   |
|-----------|---------|-------------|
| name	    | string	| Obrigatório |
| email	    | string	| Obrigatório |
| password	| string	| Obrigatório |

Funcionários - Obter Um Funcionário - (Necessário Autenticação)

    GET /api/v1/companies/employees/${id}
    
| Parâmetro	  | Tipo	  | Descrição                         |
|-------------|---------|-----------------------------------|
| id	        | number	| Obrigatório. ID de um funcionário |

Funcionários - Editar Um Funcionário - (Necessário Autenticação)
  
    PUT /api/v1/companies/employees/${id}

| Parâmetro	| Tipo	  | Descrição                                                |
|-----------|---------|----------------------------------------------------------|
| id	      | number	| Obrigatório. ID de um funcionário                        |
| groups	  | string	| Opcional. String com uma lista de ids de diversos grupos |
| name	    | string	| Opcional                                                 |
| email	    | string	| Opcional                                                 |

Funcionários - Deletar Um Funcionário - (Necessário Autenticação)
  
    DELETE /api/v1/companies/employees/${id}

| Parâmetro	| Tipo	  | Descrição                         |
|-----------|---------|-----------------------------------|
| id	      | number	| Obrigatório. ID de um funcionário |

## 📋 Documentação da API - Companies - Groups / Permissions
Grupos / Cargos - Gupos De Uma Empresa - (Necessário Autenticação)
  
    GET /api/v1/companies/groups

Grupos / Cargos - Criar Um Grupo - (Necessário Autenticação)
  
    POST /api/v1/companies/groups

| Parâmetro	  | Tipo	  | Descrição                                                       |
|-------------|---------|-----------------------------------------------------------------|
| name	      | string	| Obrigatório                                                     |
| permissions	| string	| Obrigatório. String com uma lista de ids de diversas permissões |

Grupos / Cargos - Obter Um Grupo - (Necessário Autenticação)
  
    GET /api/v1/companies/groups/${id}

| Parâmetro	| Tipo	  | Descrição                   |
|-----------|---------|-----------------------------|
| id	      | number	| Obrigatório. ID de um grupo |

Grupos / Cargos - Editar Um Grupo - (Necessário Autenticação)
  
    PUT /api/v1/companies/groups/${id}

| Parâmetro	  | Tipo	  | Descrição                                                    |
|-------------|---------|--------------------------------------------------------------|
| id	        | number	| Obrigatório. ID de um grupo                                  |
| name	      | string	| Opcional                                                     |
| permissions	| string	| Opcional. String com uma lista de ids de diversas permissões |

Grupos / Cargos - Deletar Um Grupo - (Necessário Autenticação)
  
    DELETE /api/v1/companies/groups/${id}
    
| Parâmetro	| Tipo    |	Descrição                   |
|-----------|---------|-----------------------------|
| id	      | number	| Obrigatório. ID de um grupo |

Permissões - Permissões Disponíveis - (Necessário Autenticação)
  
    GET /api/v1/companies/permissions

## 📋 Documentação da API - Companies - Tasks
Tarefas - Tarefas De Uma Empresa - (Necessário Autenticação)
  
    GET /api/v1/companies/tasks
    
Tarefas - Criar Um Tarefa - (Necessário Autenticação)
  
    POST /api/v1/companies/tasks
    
| Parâmetro	  | Tipo   |	Descrição                              |
|-------------|--------|-----------------------------------------|
| employee_id	| number |	Obrigatório. ID de um funcionário      |
| status_id	  | number |	Obrigatório. ID de um status de tarefa |
| title	      | string |	Obrigatório                            |
| description	| string |	Opcional                               |
| due_date	  | date   |	Opcional. Data no formato: d/m/Y H:M   |

Tarefas - Obter Uma Tarefa - (Necessário Autenticação)

    GET /api/v1/companies/tasks/${id}
    
| Parâmetro	| Tipo	  | Descrição                     |
|-----------|---------|-------------------------------|
| id	      | number	| Obrigatório. ID de uma tarefa |

Tarefas - Editar Um Tarefa - (Necessário Autenticação)

    PUT /api/v1/companies/tasks/${id}
    
| Parâmetro	  | Tipo	  | Descrição                            |
|-------------|---------|--------------------------------------|
| id	        | number	| Obrigatório. ID de uma tarefa        |
| employee_id	| number	| Opcional. ID de um funcionário       |
| status_id	  | number	| Opcional. ID de um status de tarefa  |
| title	      | string	| Opcional                             |
| description	| string	| Opcional                             |
| due_date	  | date	  | Opcional. Data no formato: d/m/Y H:M |

Tarefas - Deletar Uma Tarefa - (Necessário Autenticação)

    DELETE /api/v1/companies/tasks/${id}
    
| Parâmetro |	Tipo	 | Descrição                     |
|-----------|--------|-------------------------------|
| id	      | number | Obrigatório. ID de uma tarefa |
