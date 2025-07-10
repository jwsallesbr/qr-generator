# Gerador de QR Code Gratuito

Uma aplicação web e API REST para gerar QR codes customizáveis a partir de URLs, com gerenciamento de usuários. Backend em Flask, frontend em HTML/CSS.

## Funcionalidades

- ✅ **Geração de QR Codes customizáveis** (moldura, texto, cantos arredondados)
- ✅ **Download em PNG de alta qualidade**
- ✅ **Interface web responsiva**
- ✅ **API REST para integração**
- ✅ **Gerenciamento de usuários (CRUD via API)**
- ✅ **Banco de dados SQLite integrado**
- ✅ **Código aberto e gratuito**

## Como usar

### Interface Web

1. Acesse a aplicação no navegador (`http://localhost:5000`)
2. Digite a URL desejada
3. Escolha opções de moldura, texto e arredondamento
4. Clique em "Gerar QR Code"
5. Visualize e baixe o QR code gerado

### API REST

#### Gerar QR Code (base64)
`POST /api/qr/generate`

**Request:**
```json
{
  "url": "https://exemplo.com",
  "frame": "border", // opções: none, border, text
  "frame_text": "Texto opcional",
  "round_inner": "yes", // ou "no"
  "round_outer": "yes", // ou "no"
  "frame_text_size": 32
}
```
**Response:**
```json
{
  "success": true,
  "qr_code": "data:image/png;base64,...",
  "url": "https://exemplo.com"
}
```

#### Download do QR Code (PNG)
`POST /api/qr/download`

**Request:** igual ao endpoint acima, com campo opcional `file_name`.
**Response:** arquivo PNG para download.

#### Usuários (CRUD)

- `GET /api/users` — Lista todos os usuários
- `POST /api/users` — Cria usuário
  - Body: `{ "username": "nome", "email": "email@exemplo.com" }`
- `GET /api/users/<id>` — Detalha usuário
- `PUT /api/users/<id>` — Atualiza usuário
- `DELETE /api/users/<id>` — Remove usuário

## Instalação e Execução

### Pré-requisitos
- Python 3.7+
- pip

### Passos
1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   python src/main.py
   ```
4. Acesse `http://localhost:5000` no navegador

## Estrutura do Projeto

```
qr-generator/
├── src/
│   ├── main.py              # App Flask principal
│   ├── models/
│   │   └── user.py          # Modelo User (SQLAlchemy)
│   ├── routes/
│   │   ├── qr_code.py       # Rotas de QR Code (API)
│   │   └── user.py          # Rotas de Usuário (API)
│   ├── database/
│   │   └── app.db           # Banco SQLite
│   └── static/
│       ├── index.html       # Interface web
│       └── favicon.ico
├── requirements.txt         # Dependências Python
└── README.md                # Documentação
```

## Modelo de Dados

**User**
- `id`: int, chave primária
- `username`: string, único, obrigatório
- `email`: string, único, obrigatório

## Tecnologias Utilizadas
- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Frontend:** HTML, CSS
- **QR Code:** qrcode (Python)
- **Imagens:** Pillow (PIL)
- **Banco:** SQLite

## Licença

Este projeto é de código aberto e gratuito para uso pessoal e comercial.

## Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas
2. Certifique-se de que a URL fornecida é válida
3. O servidor Flask deve estar rodando na porta 5000

## Exemplos de Uso
- Compartilhar links de redes sociais
- Criar QR codes para sites pessoais
- Gerar códigos para campanhas de marketing
- Facilitar acesso a formulários online
- Compartilhar informações de contato

