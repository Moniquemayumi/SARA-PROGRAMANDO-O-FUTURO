# Guia rápido — SARA

## Requisitos

- Python 3.10 ou superior
- Acesso à internet para carregar as fontes web

## Executar no Windows / VS Code

Abra um terminal na pasta do projeto e execute:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Abra http://127.0.0.1:5000/ no navegador. Para encerrar o servidor, pressione `Ctrl+C` no terminal.

O banco SQLite é criado em `instance/denuncias.db` e permanece apenas no computador local. Não compartilhe esse arquivo: ele pode conter dados pessoais.

Para executar os testes:

```powershell
python -m unittest test_app.py -v
```

Consulte o [README principal](./README.md) para detalhes do projeto e avisos de segurança e privacidade. Este protótipo não deve receber denúncias reais.
