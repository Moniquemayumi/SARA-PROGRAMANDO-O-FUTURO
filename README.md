<div align="center">

# 🌷 SARA
### Sistema de Apoio e Registro de Assédio

**Tecnologia, acolhimento e informação para dar visibilidade a situações de assédio e discriminação no ambiente de trabalho.**

Projeto acadêmico de desenvolvimento web • Python + Flask + SQLite

</div>

---

## 💜 Sobre o projeto

O **SARA — Sistema de Apoio e Registro de Assédio** é uma aplicação web acadêmica criada para explorar como a tecnologia pode contribuir para a conscientização sobre assédio e discriminação no ambiente profissional.

A plataforma reúne, em um ambiente de demonstração, recursos para registrar relatos, consultar publicações, interagir por comentários e apoios, e visualizar dados agregados. Também contempla a participação de organizações em relatos associados ao seu nome.

O projeto busca estimular reflexão, escuta respeitosa e responsabilidade no tratamento de situações delicadas.

> **⚠️ Importante:** o SARA é um **protótipo acadêmico**, não um canal oficial de denúncias nem um serviço de atendimento ou emergência. **Não insira dados pessoais, denúncias reais ou informações sensíveis.** Antes de qualquer uso público, é necessária uma revisão de segurança, privacidade, governança e conformidade com a LGPD.

## 🎯 Objetivos

- Demonstrar uma solução digital para registro e consulta de relatos sobre o ambiente de trabalho.
- Incentivar a conscientização sobre assédio moral, assédio sexual, discriminação e outras situações relatadas.
- Explorar formas de participação e interação em uma aplicação web.
- Exibir informações agregadas para apoiar discussões e estudos.
- Aplicar conhecimentos de desenvolvimento full stack em um projeto com temática social.

## ✨ Funcionalidades implementadas

| Recurso | O que permite fazer |
| --- | --- |
| **Cadastro e login** | Criar uma conta e acessar as funcionalidades de acordo com o tipo de usuário. |
| **Publicação de relatos** | Informar título, descrição, tipo, empresa, área profissional e cidade. |
| **Opção de anonimato** | Marcar um relato como anônimo na interface. |
| **Consulta de relatos** | Visualizar publicações e seus detalhes. |
| **Filtros** | Consultar relatos por área profissional ou cidade. |
| **Comentários** | Participar das conversas nos relatos, conforme as regras de acesso implementadas. |
| **Apoios** | Adicionar ou retirar apoio a um relato; contas de empresa não podem apoiar. |
| **Área do usuário** | Consultar publicações relacionadas ao perfil. |
| **Gerenciamento** | Editar ou excluir os próprios relatos. |
| **Participação de empresas** | Contas do tipo empresa podem comentar relatos relacionados ao nome cadastrado; esses comentários são marcados como fixados. |
| **Indicadores e ranking** | Exibir contagens por categorias e uma lista de empresas por quantidade de relatos cadastrados. |

**Atenção:** o ranking reflete apenas os registros presentes no banco de dados da aplicação. Não é uma classificação oficial, não verifica a veracidade das publicações e não deve ser usado para julgar empresas ou pessoas.

## 🧭 Como utilizar o site

### 1. Acessar a página inicial
Com a aplicação executada, abra **http://127.0.0.1:5000/** no navegador. Na página inicial é possível consultar os relatos disponíveis, os indicadores e as opções de navegação.

### 2. Criar uma conta
1. Acesse a opção de **cadastro**.
2. Preencha nome, e-mail, login e senha.
3. Selecione sua área profissional e o tipo de conta disponível no formulário.
4. Finalize o cadastro para acessar a aplicação.

> Use somente dados fictícios de teste. O cadastro não representa verificação de identidade nem de vínculo empresarial.

### 3. Entrar na plataforma
1. Acesse **Login**.
2. Digite o login e a senha cadastrados.
3. Entre para visualizar os recursos associados à conta.

### 4. Registrar um relato fictício
1. Entre com uma conta do tipo **comum** ou **vítima**.
2. Acesse a opção de registro de relato.
3. Preencha título, descrição e categoria.
4. Informe, quando pertinente, empresa fictícia, área de trabalho e cidade.
5. Se desejar, marque a opção de anonimato.
6. Envie o formulário para registrar a publicação de demonstração.

**Importante:** a opção de anonimato não garante anonimato técnico. O registro continua associado a uma conta no banco de dados, e o protótipo não dispõe das proteções necessárias para uso real.

### 5. Consultar e interagir
1. Na página inicial, escolha um relato para visualizar seus detalhes.
2. Utilize os filtros de área profissional ou localização, se desejar.
3. Com uma conta habilitada, você pode comentar e adicionar ou retirar apoio.
4. Contas de empresa possuem regras específicas de interação e não podem adicionar apoio.

### 6. Consultar e gerenciar seus relatos
1. Acesse a área de **Perfil** ou **Minhas denúncias**.
2. Visualize os relatos vinculados à sua conta.
3. Utilize as opções disponíveis para editar ou excluir uma publicação de sua autoria.

### 7. Utilizar uma conta de empresa
1. Crie uma conta com o tipo de usuário **empresa**, conforme o formulário.
2. Consulte os relatos associados ao nome cadastrado.
3. Caso a condição de correspondência de nomes seja atendida, utilize o recurso de comentário.

> O protótipo faz a correspondência pelo nome cadastrado, sem autenticar oficialmente a empresa. Não representa um canal verificado de direito de resposta.

## 🛠️ Tecnologias utilizadas

| Camada | Tecnologias |
| --- | --- |
| **Back-end** | Python, Flask |
| **Banco de dados** | SQLite |
| **ORM** | Flask-SQLAlchemy, SQLAlchemy |
| **Front-end** | HTML, CSS, JavaScript e templates Jinja |
| **Testes** | `unittest` (Python) |
| **Versionamento** | Git e GitHub |

## 📁 Estrutura do projeto

```text
SARA-PROGRAMANDO-O-FUTURO/
├── app.py                 # Aplicação Flask, rotas e modelos
├── requirements.txt       # Dependências Python
├── test_app.py            # Testes automatizados
├── README.md              # Documentação principal
├── README_EXECUTAR.md     # Guia rápido de execução
├── templates/             # Páginas HTML renderizadas pelo Flask
│   ├── index.html
│   ├── login.html
│   ├── cadastrar.html
│   ├── denunciar.html
│   ├── denuncia.html
│   ├── editar.html
│   ├── perfil.html
│   └── minhas_denuncias.html
├── static/                # CSS, logo e imagens
└── instance/              # Banco SQLite local (não versionado)
```

## 🚀 Como executar o projeto no computador

### Pré-requisitos

- **Python 3.10 ou superior**;
- **Git** (para clonar o repositório);
- Terminal, PowerShell ou terminal integrado do VS Code;
- Navegador web.

### 1. Clonar o repositório

```bash
git clone https://github.com/Moniquemayumi/SARA-PROGRAMANDO-O-FUTURO.git
cd SARA-PROGRAMANDO-O-FUTURO
```

Alternativamente, baixe o projeto pela opção **Code → Download ZIP** no GitHub e extraia os arquivos.

### 2. Criar um ambiente virtual

No Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Se necessário, no Windows, use `py` no lugar de `python`. No Prompt de Comando (CMD), a ativação é `.venv\Scripts\activate.bat`.

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Iniciar o servidor

```bash
python app.py
```

### 5. Abrir o site

Acesse **http://127.0.0.1:5000/** no navegador.

O banco de dados SQLite é criado automaticamente na pasta `instance/` durante a execução. Para encerrar o servidor, pressione **Ctrl + C** no terminal.

> **Observação:** o endereço `127.0.0.1` funciona no computador onde o servidor está em execução. O fato de o código estar no GitHub não significa que exista um site publicado na internet.

## 🧪 Testes automatizados

Execute na raiz do projeto:

```bash
python -m unittest test_app.py -v
```

Os testes ajudam a verificar o comportamento das rotas e das operações principais da aplicação. Executar os testes não substitui uma auditoria de segurança.

## 🔐 Segurança, ética e privacidade

O tema do projeto envolve informações potencialmente sensíveis. Por isso, os limites da implementação atual precisam ser conhecidos:

- As senhas são tratadas sem mecanismo adequado de hash seguro.
- O controle de usuário logado utiliza estado global da aplicação, não sessões individuais seguras.
- A aplicação inicia com `debug=True` durante o desenvolvimento.
- É necessária uma revisão das autorizações, da proteção CSRF e do tratamento de entradas.
- A opção de relato anônimo não garante anonimato técnico.
- O armazenamento SQLite pode conter informações de contas e publicações: **não compartilhe o arquivo do banco**.
- Não há verificação independente da identidade de empresas nem dos relatos.
- Exibições estatísticas e rankings não representam dados oficiais ou fatos comprovados.

**Não hospede o protótipo como serviço de denúncias reais sem implementar as medidas necessárias de segurança, privacidade, moderação e conformidade com a legislação aplicável, incluindo a LGPD.**

## 🌱 Possibilidades de evolução

- Autenticação com senhas protegidas por hash e sessões seguras;
- Permissões por usuário e validação de contas empresariais;
- Controles de privacidade, minimização e retenção de dados;
- Moderação de conteúdos e mecanismos de denúncia de publicações;
- Melhorias de acessibilidade e responsividade;
- Avaliação de segurança, testes adicionais e preparação para implantação;
- Material educativo e direcionamento para canais institucionais adequados.

## 👩‍💻 Desenvolvimento

Projeto acadêmico disponível no repositório de **[Monique Mayumi](https://github.com/Moniquemayumi)**.

🔗 **Repositório:** https://github.com/Moniquemayumi/SARA-PROGRAMANDO-O-FUTURO

---

<div align="center">

### 💜 SARA — Tecnologia a serviço da conscientização

*Ouvir, informar e conscientizar também fazem parte da transformação.*

</div>
