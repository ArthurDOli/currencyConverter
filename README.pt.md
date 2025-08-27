# Conversor de Moedas

Um conversor de moedas desenvolvido em Python utilizando a ExchangeRate API.
Permite consultar taxas de câmbio em tempo real e converter valores entre diferentes moedas de forma simples e rápida.

## Funcionalidades

- Conversão de moedas em tempo real
- Integração com a ExchangeRate API
- Opção para gerar um executável (.exe)
- Tratamento de errors e validação de entradas

## Instalação

Após clonar o repositório, crie um ambiente virtal com:

```bash
python -m venv venv
```

Após isso, ative o ambiente virtual, instale as dependências com:

```bash
pip install -r requirements.txt
```

Por fim, configure a sua API criando um arquivo .env na raiz do projeto e coloque:

```bash
API_KEY = sua chave
```

## Como criar um executável

Caso queira criar um arquivo executável desse projeto, utilize a biblioteca PyInstaller (que já esta instalada) e rode o seguinte comando no terminal:

```bash
pyinstaller --onefile --console main.py
```
