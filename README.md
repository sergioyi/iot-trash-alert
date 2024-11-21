#   Criando um projeto Django

```Dockerfile
FROM postgres:16 
ENV POSTGRES_DB=lixo 
ENV POSTGRES_USER=postgres 
ENV POSTGRES_PASSWORD=postgres 
## para variáveis de ambiente, caso precise do psycopg2 
ENV PG_CONFIG=/usr/bin/pg_config 

EXPOSE 5432 
CMD ["postgres"] 
#   docker build -t postgres_lixo:lateste .
#   docker run -d --name postgres_lixo_c postgres_lixo:lateste
#   docker start postgres_lixo_c
#   docker stop postgres_lixo_c


#   docker ps -a
#   docker images

```

Ambiente de desenvolvimento
```shell
python3 -m venv venv
```
Iniciando o ambiente
```shell
source ./venv/bin/activate
```
Instalando o Django no ambiente
```shell
python -m pip install Django
```
Criando um projeto 
```shell
django-admin startproject personal_iot .
```
Iniciando o projeto
```shell
python manage.py runserver
```

Inicializando um app no seu projeto
```shell
python3 manage.py startapp lux
```

Depois de criar, é necessário deixar o Django saber que 
esse app existe, adicionando-o na lista de apps\
Dentro de personal_iot/settings.py adicionar:
```python
INSTALLED_APPS = [
"lux.apps.LuxConfig",
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
]
```
Dentro de lux/view.py adicionar
```python
# lux/views.py
from django.shortcuts import render
def home(request):
    return render(request, "lux/home.html", {})
# Aqui foi criado um código responsável por renderizar um arquivo html chamado “home.html”.
```
Agora vamos criar uma subpasta chamada\
templates e um arquivo html chamado home.html\
mkdir -p lux/templates/lux\
echo > lux/templates/lux/home.html  “

Dentro do arquivo home.html vamos adicionar:
<!-- pages/templates/pages/home.html -->
```html
<h1>Hello, World!</h1>
```

Faça as modificações no arquivo urls.py
```python
from django.contrib import admin
from django.urls import path
, include
urlpatterns = [
path('admin/', admin.site.urls),
path("", include("lux.urls")),
]
```
lux.urls ainda não existe, vamos criar\
echo > lux/urls.py
```python
# lux/urls.py
from django.urls import path
from lux import views
urlpatterns = [
    path("", views.home, name='home'),
]
```
dê uma olhada funcionando
```shell
python manage.py runserver
```






#   ChatGpt ajuda com o psycopg2

Para disponibilizar o banco de dados PostgreSQL rodando no container para o seu projeto Django (fora do container), você não precisa configurar o PG_CONFIG no host manualmente, pois o psycopg2 utiliza as bibliotecas de desenvolvimento do PostgreSQL localizadas no host onde o ambiente virtual (venv) está instalado.

Aqui está o passo a passo para garantir que tudo funcione corretamente:
1. Garanta que o container está funcionando

Certifique-se de que o container do PostgreSQL está rodando. O comando para verificar isso é:

```shell
docker ps
```

Caso o container não esteja rodando, inicie-o:

```shell
docker start postgres_lixo_c
```

2. Conecte-se ao banco via host

Quando você criou o container com docker run, o PostgreSQL foi configurado para escutar na porta padrão (5432) e pode ser acessado no host do Docker.

Se você usou o comando sugerido (docker run --name postgres_lixo_c), o container PostgreSQL estará acessível na porta padrão. Certifique-se de mapear as portas ao rodar o container:

```shell
docker run -d --name postgres_lixo_c -p 5432:5432 postgres_lixo:lateste
```

Isso mapeia a porta 5432 do container para a porta 5432 do seu host.

3. Confirme o mapeamento da porta

Verifique se a porta 5432 do container foi mapeada corretamente para o host. Você pode verificar isso no comando docker ps. A coluna PORTS deve mostrar algo como 0.0.0.0:5432->5432/tcp.
Confirme o IP ou Host

Certifique-se de que o endereço no settings.py está correto.

    Localmente (Docker no mesmo sistema): Use 127.0.0.1.
    Se o Docker estiver em outro sistema: Use o IP do servidor Docker.

Você pode verificar o IP do container com:

```shell
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_lixo_c
```

Isso retornará o IP interno do container (exemplo: 172.17.0.2). Atualize o settings.py para usar este IP como HOST:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lixo',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '172.17.0.2',  # Substitua pelo IP retornado
        'PORT': '5432',
    }
}
```
4. Instalar o psycopg2

No seu ambiente virtual Python (venv), instale o psycopg2 para permitir a comunicação entre o Django e o PostgreSQL. Execute o seguinte comando:

```shell
pip install psycopg2-binary
```

5. Testar a conexão

Depois de configurar o banco e o psycopg2, teste a conexão com o comando do Django:

```shell
python manage.py makemigrations
python manage.py migrate
```

Se não houver erros, a conexão com o banco de dados estará funcionando.
Observação sobre PG_CONFIG

O PG_CONFIG é necessário apenas para compilar extensões nativas ou instalar o psycopg2 sem a versão binária. No Linux Mint, certifique-se de que as bibliotecas de desenvolvimento do PostgreSQL estão instaladas no host:

```shell
sudo apt update
sudo apt install libpq-dev
```

Se já instalou o psycopg2-binary, não precisa se preocupar com o PG_CONFIG, pois ele já inclui os binários necessários.


https://chatgpt.com/share/673e44d2-5fa4-8011-ae06-76d1b4d950a3

#   Segundo commit comandos
Intalação do mqtt:

```shell
pip install paho-mqtt

```
Iniciar a aplicação:
```shell
python manage.py start_mqtt
```