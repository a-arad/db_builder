def generate_table_command(table_name, columns):
    """generates a SQL CREATE TABLE command."""
    column_defs = []
    primary_keys = []
    for col in columns:
        col_def = f"{col['column']} {col['data_type']}"
        if col['primary_key'] == 1:
            primary_keys.append(col['column'])
        column_defs.append(col_def)
    
    primary_key_def = ', '.join(primary_keys)
    column_defs_str = ', '.join(column_defs)
    
    drop_statement = f"DROP TABLE IF EXISTS {table_name};"

    if primary_keys:
        create_statement =  f"CREATE TABLE {table_name} ({column_defs_str}, PRIMARY KEY ({primary_key_def}));"
    else:
        create_statement =  f"CREATE TABLE {table_name} ({column_defs_str});"

    return f"{drop_statement}\n{create_statement}"