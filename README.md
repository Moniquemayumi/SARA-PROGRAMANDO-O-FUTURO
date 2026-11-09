# S.A.R.A. — Sistema de Apoio e Registro de Assédio

> **Quebre o silêncio. Sua voz importa.**

A **S.A.R.A.** é um projeto de plataforma web voltado ao registro e à visualização de denúncias de assédio e discriminação no ambiente de trabalho. A proposta é incentivar a escuta, a conscientização e a transparência, reunindo relatos e informações em um mesmo espaço digital.

**Status:** protótipo acadêmico / em desenvolvimento. O sistema não substitui canais oficiais de denúncia, acolhimento profissional ou orientação jurídica.

## 🎯 Objetivo

Criar um ambiente digital no qual pessoas possam compartilhar experiências relacionadas a assédio moral, assédio sexual e discriminação salarial no trabalho, além de consultar relatos, interagir com publicações e identificar padrões nas informações registradas.

## ✨ Funcionalidades presentes no código

- **Cadastro e login:** criação de contas com diferentes tipos de usuário.
- **Registro de denúncias:** título, descrição, categoria, empresa, área profissional e cidade.
- **Opção de publicação anônima:** permite solicitar a ocultação do nome em uma publicação.
- **Consulta de relatos:** listagem de denúncias e visualização de detalhes.
- **Interações:** comentários e apoio a denúncias, com opção de remover o apoio.
- **Perfil:** visualização de denúncias relacionadas à conta.
- **Gerenciamento de relatos próprios:** edição e exclusão.
- **Filtros:** consulta de denúncias por área profissional e cidade.
- **Ranking de empresas:** listagem das empresas por quantidade de denúncias cadastradas, limitada às dez primeiras.
- **Interação de empresas:** lógica para respostas de contas identificadas como empresa nas denúncias associadas ao seu nome.

> **Importante:** o ranking apresenta apenas a quantidade de relatos registrados na aplicação. Ele não comprova a ocorrência de irregularidades nem deve ser interpretado como avaliação oficial de empresas. O código também não implementa verificação independente dos relatos.

## 🛠️ Tecnologias

| Camada | Tecnologias |
| --- | --- |
| Backend | Python, Flask |
| Persistência | SQLite, Flask-SQLAlchemy |
| Frontend | HTML5, CSS3, JavaScript |
| Templates | Jinja2 (via Flask) |

## 🗂️ Estrutura do repositório

```text
SARA-PROGRAMANDO-O-FUTURO/
├── app.py                # Rotas, modelos e regras do backend
├── index.html             # Página inicial
├── login.html             # Login
├── cadastrar.html         # Cadastro
├── denunciar.html         # Formulário de denúncia
├── denuncia.html          # Detalhes e interações
├── perfil.html            # Perfil de usuário
├── editar.html            # Edição de denúncia
├── minhas_denuncias.html  # Listagem de denúncias próprias
├── *.css                  # Estilos das páginas
└── README.md              # Documentação do projeto
```

O repositório também contém outros arquivos HTML, como `cadastro.html`, `nova_denuncia.html` e `denunciar.html`, que representam versões ou telas adicionais.

## 💻 Como executar localmente

**Pré-requisitos:** Python 3 e pip.

1. Clone o repositório:

```bash
git clone https://github.com/Moniquemayumi/SARA-PROGRAMANDO-O-FUTURO.git
cd SARA-PROGRAMANDO-O-FUTURO
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

Windows (PowerShell):
```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:
```bash
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install Flask Flask-SQLAlchemy
```

4. **Antes de executar**, organize os arquivos para o padrão esperado pelo Flask: mova os HTML usados por `render_template` para a pasta `templates/`, e os CSS para `static/`. Verifique os caminhos de `url_for('static', ...)` nos HTML, pois há referências a caminhos diferentes.

5. Inicie a aplicação:

```bash
python app.py
```

6. Acesse **http://127.0.0.1:5000/**.

**Nota:** na versão consultada, os HTML e CSS estão na raiz do repositório, embora o backend utilize os diretórios convencionais do Flask. Portanto, o projeto precisa desse ajuste de estrutura para funcionar corretamente; também podem existir links e telas que precisam de integração. O banco SQLite é criado durante a inicialização pelo código da aplicação.

## 🧩 Modelos de dados

O backend define quatro modelos principais:

- **Usuario:** dados da conta, área profissional e tipo de perfil.
- **Denuncia:** informações do relato, localidade, anonimato e número de apoios.
- **Apoio:** associação entre usuário e denúncia apoiada.
- **Comentario:** mensagens relacionadas às denúncias.

## 🔒 Privacidade, segurança e responsabilidade

O projeto trata de informações potencialmente sensíveis. **A implementação atual é demonstrativa e não deve receber denúncias reais nem ser disponibilizada publicamente sem revisão de segurança.**

Antes de um lançamento real, será necessário:

- Armazenar senhas com hash seguro, nunca em texto puro.
- Implementar autenticação por sessão, eliminando identificadores globais de usuário e de denúncia.
- Proteger formulários e operações contra CSRF e validar permissões no servidor.
- Garantir que publicações marcadas como anônimas realmente não revelem a identidade da pessoa nos conteúdos exibidos, logs ou respostas da aplicação.
- Revisar coleta, retenção, exclusão e acesso a dados pessoais em conformidade com a LGPD.
- Implementar moderação e mecanismos para contestação de relatos e prevenção de exposição indevida.
- Desativar o modo `debug=True` fora do desenvolvimento local.
- Realizar testes funcionais, de segurança, privacidade e acessibilidade.

A opção de anonimato existente no código **não constitui garantia de anonimato técnico**.

## 🚀 Próximas melhorias

- [ ] Reorganizar templates e arquivos estáticos para a estrutura Flask.
- [ ] Revisar e corrigir rotas e links entre páginas.
- [ ] Implementar autenticação segura e autorização por usuário.
- [ ] Revisar a apresentação de denúncias anônimas.
- [ ] Adicionar validações e mecanismos de moderação.
- [ ] Melhorar responsividade e acessibilidade da interface.
- [ ] Criar testes automatizados.
- [ ] Documentar o processo de implantação.
- [ ] Desenvolver indicadores confiáveis, respeitando privacidade e contexto dos relatos.

## 💜 Impacto social

A S.A.R.A. nasce da ideia de que a tecnologia pode contribuir para ambientes profissionais mais seguros, oferecendo ferramentas de registro, visibilidade e conscientização. Seu propósito é unir desenvolvimento de software e responsabilidade social, sem perder de vista a proteção de quem compartilha experiências.

---

**Repositório:** [Moniquemayumi/SARA-PROGRAMANDO-O-FUTURO](https://github.com/Moniquemayumi/SARA-PROGRAMANDO-O-FUTURO)

**Aviso:** projeto em desenvolvimento, para fins de aprendizagem e demonstração.