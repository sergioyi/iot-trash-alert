# iot-trash-alert

## Requisitos de configuração:
- VS Code
    - python instalado
    - psycopg2
- Arduino IDE
    - esp32
    - Ultrasonic
    - PubSubClient
    - projeto montado
    - modifique seu [acesso ao wi-fi](./sensor_de_proxim/sensor_de_proxim.ino#L10).
- Banco de dados
    - Deve estar em execução
    - Você pode instalá-lo localmente e reconfigurar as [configurações de conexão da aplicação](./two.py#L10), O projeto já está configurado para Docker. Segue o Dockerfile:

 ```Dockerfile
FROM postgres:latest

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=lixo

EXPOSE 5432

## docker build -t meu_postgres .
## docker run -d --name postgres_container -p 5432:5432 meu_postgres
```
\
    - crie a tabela usando a [query](./queries.sql)
    - o código do python a ser executado é o two.py, não precisa usar a pasta prof

## Como funciona atualmente:
Seguindo o último envio de desafio do professor Pablo, o projeto deve enviar dados para o banco de dados. Execute os dois projetos ao mesmo tempo e aproxime-se do sensor de presença a uma distância de, no máximo, 3 cm.
