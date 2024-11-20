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
