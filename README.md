Agenda de Treinos

Integrantes:
Marianne Júlia Ferreira dos Santos
Lívia Vitória Guadalupe de Souza Faria
Evelyn Ester Azevedo Brito
Kessya Cauanny de Araújo Costa
Ludimila Erika Silva de Araújo


Descrição:

Este projeto consiste no desenvolvimento de uma aplicação web para gerenciamento de itens relacionados a treinos e atividades físicas. A aplicação permite cadastrar, listar, editar, excluir e alterar o status dos itens, além de possibilitar filtragens.

O sistema foi desenvolvido utilizando Python com Flask no backend, banco de dados SQLite e frontend em HTML, CSS e JavaScript puro.


Objetivo:

Permitir o controle e organização de atividades físicas, registrando treinos e provas esportivas, mantendo informações organizadas e persistentes.

Modelo de Dados
Entidade: Item
Campo	Tipo	Obrigatório	Descrição
id	inteiro	Sim	Identificador único
titulo	texto	Sim	Nome do treino
tipo	texto	Sim	Categoria do treino
status	texto	Sim	Situação do treino
data	texto	Opcional	Data do treino (YYYY-MM-DD)
valor	número	Opcional	Valor associado ao treino

Tipos Permitidos:
caminhada
rua
meia-maratona
maratona

Status Permitidos:
ativo
concluido
cancelado

Funcionalidades:
Backend
Listar itens
Criar item
Editar item
Excluir item
Alterar status
Validação de dados
Persistência em banco SQLite
Tratamento de erros
API REST
Frontend
Tela única
Cadastro e edição de itens
Listagem em tabela
Exclusão de itens
Alteração de status
Filtros por tipo e status
Mensagens de erro e sucesso
Indicador de carregamento

Endpoints da API:
Listar itens
GET /items


Filtros opcionais:
GET /items?tipo=caminhada
GET /items?status=ativo

Criar item
POST /items


Exemplo JSON:

{
  "titulo": "Treino longo",
  "tipo": "rua",
  "status": "ativo",
  "data": "2026-02-04",
  "valor": 50
}

Editar item
PUT /items/:id

Alterar status
PATCH /items/:id/status

Excluir item
DELETE /items/:id

Validações Implementadas
Título mínimo de 3 caracteres
Tipo deve estar na lista permitida
Status deve estar na lista permitida
Valor deve ser maior ou igual a zero
Data deve estar no formato YYYY-MM-DD
Persistência
Os dados são armazenados em banco SQLite localizado em:
instance/agenda.db

Como Executar o Projeto:
Clonar o repositório
git clone <https://github.com/mariannejj/projetopsi4>
Criar ambiente virtual
python -m venv venv
Ativar ambiente virtual

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

Instalar dependências
pip install flask flask-cors ou pip install -r requeriments.txt

cd backend e flask run --debug

Acessar no navegador
http://localhost:5000

Tecnologias Utilizadas:
Python
Flask
SQLite
HTML5
CSS3
JavaScript
Fetch API


Estrutura do Projeto
PROJETOPSI4/
│
├── backend/
│   ├── instance/
│   │   └── agenda.db
│   │
│   ├── app.py
│   ├── db.py
│   ├── items.py
│   └── settings.py
│
├── web/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── README.md
├── requirements.txt


Testes Realizados:
Foram realizados testes utilizando navegador web e requisições utilizando Fetch API.
Autenticação de usuários
Interface responsiva



Licença:
Projeto desenvolvido para fins acadêmicos.