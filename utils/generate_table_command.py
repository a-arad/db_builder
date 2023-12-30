def generate_table_command(table_name, columns):
    """generates a SQL CREATE TABLE command."""
    column_defs = []
    primary_keys = []
    for col in columns:
        col_def = f"{col['column']} {col['data type']}"
        if col['primary key'] == 1:
            primary_keys.append(col['column'])
        column_defs.append(col_def)
    
    primary_key_def = ', '.join(primary_keys)
    column_defs_str = ', '.join(column_defs)
    
    if primary_keys:
        return f"CREATE TABLE {table_name} ({column_defs_str}, PRIMARY KEY ({primary_key_def}));"
    else:
        return f"CREATE TABLE {table_name} ({column_defs_str});"