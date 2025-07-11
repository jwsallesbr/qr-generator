# 🧩 Gerador de QR Code

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](...)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Uma aplicação web e API REST para gerar QR codes customizáveis a partir de URLs.

## 🎯 Funcionalidades

- ✅ **Geração de QR Codes customizáveis** (moldura, texto, cantos arredondados, tamanho do texto)
- 🖼️ **Download em PNG de alta qualidade**
- 📱 **Interface web responsiva com modo claro/escuro**

## 🛠️ Pré-requisitos
- 🐍 Python 3.7 ou superior
- 📦 pip (gerenciador de pacotes Python)

## 🚀 Iniciando

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/jwsallesbr/qr-generator.git
   cd qr-generator
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   python src/main.py
   ```
   > ⚡ Se tudo estiver correto, você verá uma mensagem como:
   > `* Running on http://0.0.0.0:5000/`

### 🌐 Acesse a interface web:
   ```bash
   http://localhost:5000
   ```

- Adicione a URL que deseja converter em QR Code.
- Escolha as opções de personalização (moldura, texto, arredondamento, tema).
- Clique em **"Gerar QR Code"**.
- Visualize o QR Code gerado na tela.
- Clique em **"Baixar PNG"** para salvar o QR Code no seu computador.

---

### ⚡ API REST

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
  "frame_text_size": 32 // valor entre 10 e 54
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