from utils.generate_table_command import generate_table_command

def generate_sql_commands(schema):
    """generates SQL commands for all tables in the schema."""
    commands = []
    for table, columns in schema.items():
        command = generate_table_command(table, columns)
        commands.append(command)
    return commands
