import psycopg2
from psycopg2 import sql

def execute_sql_commands(sql_commands, tables_data,db_connection_string):
    '''connect to neon and execute sql commands'''
    conn = psycopg2.connect(db_connection_string)

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