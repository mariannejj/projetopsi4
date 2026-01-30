Agenda de Treinos

A Agenda de Treinos é um  mini-sistema de registros para organização de treinos de atletas que permite cadastrar, editar, listar e gerenciar atividades físicas como corrida, caminhada e treino funcional, facilitando o controle da rotina esportiva.
O projeto foi desenvolvido no modelo API + Frontend, com uma única entidade principal, conforme o contrato do projeto proposto para o Ensino Médio Técnico.

Categoria: Saúde
Tema: Agenda de Treinos (Atletas)

Entidade única: Item
Campos obrigatórios: id (number), titulo (string, mínimo 3 caracteres),tipo (string) e status (string).
Campos opcionais utilizados: descrição (string) e data (string no formato YYYY-MM-DD).

Tipos: corrida ,caminhada, maratona e meio maratona.
Status: ativo, concluído e cancelado

API — Endpoints
Base URL: http://localhost:5000
GET /items
GET /items?tipo=corrida
GET /items?status=planejado
POST /items
PUT /items/:id
PATCH /items/:id/status
DELETE /items/:id

Título é obrigatório e deve ter no mínimo 3 caracteres,tipo deve estar dentro da lista permitida; Status deve estar dentro da lista permitida; Data, quando informada, deve estar no formato YYYY-MM-DD.
Exemplo de erro:
  "error": "título é obrigatório e deve ter no mínimo 3 caracteres"

Os dados são armazenados em um arquivo items.json, garantindo que as informações não sejam perdidas ao reiniciar o servidor.
Frontend
O sistema possui uma única tela com formulário para criar e editar treinos, lista de treinos cadastrados, ações de editar, remover e mudar status, filtros por tipo e status.
O frontend consome a API utilizando fetch ou axios.
Como Executar
Backend: Instalar Python 3, criar e ativar ambiente virtual, Instalar dependências do requirements.txt, executar o arquivo principal da aplicação
Frontend: Instalar dependências com npm e executar o projeto com npm run dev

Autores
Evelyn Ester Azevedo Brito
Lívia Vitória Guadalupe Souza Faria
Marianne Júlia Ferreira dos Santos
Ludimila Érica Silva de Araújo
Kessya Cauanny Araújo Costa
