# Gerador de QR Code Gratuito

Uma aplicação web simples e gratuita para gerar QR codes a partir de URLs.

## Características

- ✅ **Totalmente gratuito** - Sem custos ou limitações
- ✅ **Sem limite de uso** - Gere quantos QR codes precisar
- ✅ **Download em alta qualidade** - Imagens PNG de alta resolução
- ✅ **Interface responsiva** - Funciona em desktop e mobile
- ✅ **Sem registro necessário** - Use imediatamente
- ✅ **Código aberto** - Totalmente transparente

## Como usar

### Interface Web

1. Acesse a aplicação no navegador
2. Digite a URL que deseja converter em QR code
3. Clique em "Gerar QR Code"
4. Visualize o QR code gerado
5. Clique em "Baixar PNG" para salvar a imagem

### Script Python (linha de comando)

```python
from generate_qr import generate_qr_code

# Gerar QR code para uma URL
generate_qr_code("https://www.exemplo.com", "meu_qr.png")
```

## Instalação e Execução

### Pré-requisitos

- Python 3.7+
- pip

### Passos

1. Clone ou baixe os arquivos
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   cd qr_generator
   source venv/bin/activate  # Linux/Mac
   python src/main.py
   ```
4. Acesse `http://localhost:5000` no navegador

## Estrutura do Projeto

```
qr_generator/
├── src/
│   ├── main.py              # Aplicação Flask principal
│   ├── routes/
│   │   └── qr_code.py       # Rotas da API
│   └── static/
│       └── index.html       # Interface web
├── requirements.txt         # Dependências Python
└── README.md               # Esta documentação
```

## API Endpoints

### POST /api/qr/generate
Gera um QR code e retorna como base64.

**Request:**
```json
{
  "url": "https://exemplo.com"
}
```

**Response:**
```json
{
  "success": true,
  "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  "url": "https://exemplo.com"
}
```

### POST /api/qr/download
Gera um QR code e retorna como arquivo PNG para download.

**Request:**
```json
{
  "url": "https://exemplo.com"
}
```

**Response:** Arquivo PNG

## Tecnologias Utilizadas

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **QR Code:** Biblioteca `qrcode` do Python
- **Imagens:** Pillow (PIL)

## Licença

Este projeto é de código aberto e gratuito para uso pessoal e comercial.

## Suporte

Para dúvidas ou problemas, verifique se:
1. Todas as dependências estão instaladas
2. A URL fornecida é válida
3. O servidor Flask está rodando na porta 5000

## Exemplos de Uso

- Compartilhar links de redes sociais
- Criar QR codes para sites pessoais
- Gerar códigos para campanhas de marketing
- Facilitar acesso a formulários online
- Compartilhar informações de contato

