import sys
from utils import (
    parse_schema, 
    generate_sql_commands, 
    read_csv_files, 
    execute_sql_commands
                   )

csv_folder_path = sys.argv[1]
db_connection_string = sys.argv[2]

schema = parse_schema(f"{csv_folder_path}/schema.csv")
sql_commands = generate_sql_commands(schema)
tables_data = read_csv_files(csv_folder_path)
execute_sql_commands(sql_commands, tables_data, db_connection_string)