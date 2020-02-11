# Instalação da API


## Clone

1. Clonar o repo para um diretório local

---

## Configurar virtual enviroment

Dentro do diretório do projeto, criar e ativar o virtual enviroment.

1. virtualenv venv
2. source venv/bin/activate

---

## Instalar dependências

1. pip install -r requirements.txt

---

## Configurar o postgres

Criar database e usuário do postgres

1. **Comando para inciar o postgres:** psql

2. CREATE DATABASE estagio_web;
3. CREATE USER postgres;
4. GRANT ALL PRIVILEGES ON DATABASE estagio_web TO postgres;

5. **Comando para sair do postgres:** \q

---

## Config.py do projeto

Verificar se o nome do database no arquivo de configurações do projeto corresponde ao que foi criado

1. SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/estagio_web'

---

## Startar o DB no postgres

Processo realizado na UI do postgres

---

## Update no DB da aplicação e iniciar o servidor

1. ./utils_gen/update_database.sh
2. ./utils_gen/start_server.sh 

---

## Popular o DB

Através do pgAdmin, executar o escript abaixo no DB da Api.

