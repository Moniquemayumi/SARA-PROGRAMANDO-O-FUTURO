# SARA — Sistema de Apoio e Registro de Assédio

Aplicação web acadêmica em Python, Flask, SQLAlchemy e SQLite para registro e consulta de relatos de assédio e discriminação no ambiente de trabalho.

> **Aviso:** este projeto é um protótipo. Não o use para receber denúncias reais nem o publique como serviço sem revisão de segurança e privacidade.

## Estrutura

```text
├── app.py
├── requirements.txt
├── test_app.py
├── README.md
├── README_EXECUTAR.md
├── templates/                 # Páginas Flask com Jinja
├── static/
│   ├── css/sara-theme.css
│   ├── images/                # Logo e imagens usadas pela interface
│   └── logo-sara.svg
└── instance/                  # Banco SQLite local, não versionado
```

## Executar localmente

Requer Python 3.10 ou superior.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Acesse http://127.0.0.1:5000/.

O SQLite é criado localmente em `instance/denuncias.db`. Esse arquivo pode conter relatos e dados de conta; o `.gitignore` impede que ele seja enviado ao GitHub.

## Testes

```powershell
python -m unittest test_app.py -v
```

A suíte cobre rotas principais, operações de relatos e o modo de demonstração. Os exemplos do modo de demonstração são fictícios e não são gravados no banco.

## Segurança e privacidade

A implementação atual é apenas demonstrativa. Antes de qualquer uso real, é necessário implementar armazenamento seguro de senhas, sessões adequadas, proteção CSRF, controle de permissões e revisar a coleta e retenção de dados conforme a LGPD. O ranking representa somente os registros da aplicação; não comprova irregularidades nem constitui avaliação oficial de organizações.
