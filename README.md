# Weather API FastAPI 🌤️

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-green.svg)](https://fastapi.tiangolo.com/)
[![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-orange.svg)](https://openweathermap.org/api)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Uma API moderna e eficiente para consulta de dados meteorológicos, construída com FastAPI e integrada com OpenWeatherMap. Oferece respostas em português e sistema de cache inteligente.

## ✨ Funcionalidades

- 🔍 Consulta de dados meteorológicos por cidade
- 🚀 Cache inteligente para otimização de performance
- 🇧🇷 Respostas em português
- 🌡️ Temperaturas em Celsius
- 📚 Documentação automática com Swagger UI
- ✅ Validação de dados com Pydantic

## 🚀 Tecnologias

- [Python 3.9+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [OpenWeatherMap API](https://openweathermap.org/api)

## 📋 Pré-requisitos

- Python 3.9 ou superior
- Chave de API do OpenWeatherMap
- pip (gerenciador de pacotes Python)

## ⚙️ Configuração

### 1. Clone o repositório
```bash
git clone git@github.com:camylla-ops/weather-api-fastapi.git
cd weather-api-fastapi
```

### 2. Configure o ambiente virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
1. Copie o arquivo de template:
```bash
cp .env-template .env
```

2. Obtenha sua chave API:
   - Crie uma conta em [OpenWeatherMap](https://openweathermap.org/)
   - Acesse [API Keys](https://home.openweathermap.org/api_keys)
   - Copie sua chave API

3. Configure o arquivo `.env`:
```env
OPENWEATHERMAP_API_KEY=sua_chave_de_32_caracteres
CACHE_TTL=300
```

## 🚀 Uso

### Iniciando o servidor
```bash
uvicorn app:app --reload
```

### Acessando a API
- **Documentação Swagger UI**: http://localhost:8000/docs
- **Documentação ReDoc**: http://localhost:8000/redoc

### Exemplo de requisição
```bash
curl "http://localhost:8000/weather?city=São Paulo"
```

### Exemplo de resposta
```json
{
    "cidade": "São Paulo",
    "temperatura": 25.6,
    "temperatura_min": 23.2,
    "temperatura_max": 27.8,
    "umidade": 65,
    "descricao": "céu limpo",
    "atualizado_em": "2024-02-20 14:30:45"
}
```

## 🔧 Cache

O sistema de cache foi implementado para otimizar o desempenho e reduzir chamadas desnecessárias à API externa:

- ⏱️ TTL (Time To Live) padrão: 5 minutos
- 💾 Capacidade: 100 cidades
- ⚡ Atualização automática após expiração

## 📚 Documentação da API

A API oferece documentação interativa completa:

- **Swagger UI**: http://localhost:8000/docs
  - Interface interativa para teste
  - Documentação detalhada dos endpoints
  - Exemplos de requisição/resposta

- **ReDoc**: http://localhost:8000/redoc
  - Documentação técnica detalhada
  - Referência completa da API

## ❗ Solução de Problemas

### Erro 401 (Unauthorized)
1. Verifique se a chave API foi copiada corretamente
2. Certifique-se de que não há espaços na chave
3. Aguarde a ativação da chave (pode levar até 2 horas)
4. Confirme a localização do arquivo `.env`

### Outros Problemas
- Verifique se todas as dependências estão instaladas
- Confirme que está usando Python 3.9+
- Verifique se o ambiente virtual está ativo

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia nosso guia de contribuição antes de submeter mudanças.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


---
⭐ Se este projeto te ajudou, considere dar uma estrela! 