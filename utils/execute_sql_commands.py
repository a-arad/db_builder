import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv, find_dotenv

def execute_sql_commands(sql_commands, tables_data):
    '''connect to neon and execute sql commands'''
    _ = load_dotenv(find_dotenv())  # read in credentials

    conn = psycopg2.connect(
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST']
    )

    try:
        with conn.cursor() as cur:
            for command in sql_commands:
                cur.execute(command)
            
            for table, data in tables_data.items():
                insert_query = sql.SQL("INSERT INTO {} VALUES %s").format(sql.Identifier(table))
                psycopg2.extras.execute_values(cur, insert_query, data.to_records(index=False))
            
            conn.commit() 
    except Exception as e:
        conn.rollback() 
        raise e
    finally:
        conn.close()