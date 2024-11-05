import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

#connection = create_connection(
#    "lixo", "root", "admin", "localhost", "5432"
#)

def db_insert(valores):
  insert_query = (
      f'INSERT INTO public."tb_mensagem" ("mensagem") VALUES ('+f"'{valores}'"+f') RETURNING "id"'
  )
  with create_connection("lixo", "root", "admin", "localhost", "5432") as con:
      with con.cursor() as cur:
        cur.execute(insert_query)
        hundred = cur.fetchone()[0]
      con.commit()
  print(hundred)