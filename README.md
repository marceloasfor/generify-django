# Python / Django

Versão do Django: 4.0.4
Versão do Python: 3.10.4

# Setup inicial

### Banco de Dados
1. Instale o Postgres
2. Crie um usuário e senha para o postgres
3. Crie um banco de dados postgres

### Django Setup
1. Dê um pull no projeto
2. Crie um ambiente python: `python3 -m venv /path/to/new/virtual/environment`
3. Certifique-se que está no ambiente python: `source <venv>/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`

### Django Config
1. Configure o login e senha do banco de dados no arquivo settings.py, na seção adequada.
2. Crie um superusuário para você com o comando (dentro de webapp) `python manage.py createsuperuser`
3. Certificado que seu banco de dados está online, rode as migrations: `python manage.py makemigrations`

### Iniciar o serviço
1. `python manage.py runserver 8080`