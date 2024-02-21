import subprocess

def execute_with_psql(sql_file, db_connection_string):
    '''runs the sql file '''
    psql_command = f"psql {db_connection_string} -f {sql_file}"
    subprocess.run(psql_command, shell=True, check=True)

if __name__ == "__main__":

    import sys
    execute_with_psql(sql_file=sys.argv[1],db_connection_string=sys.argv[1])