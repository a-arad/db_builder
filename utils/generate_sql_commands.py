import os
from utils.generate_table_command import generate_table_command

def generate_sql_commands(schema,folder_path):
    """generates SQL commands for all tables in the schema."""
    def create_copy_command(table_name, file_path):
        '''adds psql copy command'''
        return f"\copy {table_name} FROM '{file_path}' DELIMITER ',' CSV HEADER NULL AS ''"
    commands = ""
    for table, columns in schema.items():
        commands += generate_table_command(table, columns) + ";\n"
        # assumes file names match table names
        csv_file_path = os.path.join(folder_path, f"{table}.csv")
        commands += create_copy_command(table, csv_file_path) + "\n"
    sql_script_path = f'create_{os.path.basename(folder_path)}.sql'
    with open(sql_script_path, 'w') as f:
      f.write(commands)
    return sql_script_path
