import sys
from utils import (
    parse_schema, 
    generate_sql_commands, 
    execute_with_psql
                   )

csv_folder_path = sys.argv[1]
db_connection_string = sys.argv[2]

schema = parse_schema(f"{csv_folder_path}/schema.csv")
sql_file_path = generate_sql_commands(schema)
execute_with_psql(sql_file_path,db_connection_string)