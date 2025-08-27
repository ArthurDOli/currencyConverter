# Currency Converter

A currency converter developed in Python using the ExchangeRate API.  
It allows you to check real-time exchange rates and convert values between different currencies quickly and easily.

## Features

- Real-time currency conversion
- Integration with the ExchangeRate API
- Option to generate an executable (.exe)
- Error handling and input validation

## Installation

After cloning the repository, create a virtual environment with:

```bash
python -m venv venv
```

Then, activate the virtual environment and install the dependencies:

```bash
pip install -r requirements.txt
```

Finally, configure your API key by creating a .env file in the project root and adding:

```bash
API_KEY = sua chave
```

## How to create an executable

If you want to generate an executable for this project, use the PyInstaller library (already included in the dependencies) and run the following command in the terminal:

```bash
pyinstaller --onefile --console main.py
```
