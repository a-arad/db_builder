import os
import pandas as pd

def read_csv_files(folder_path, schema_file='schema.csv'):
    '''reads the target data into a dictionary
       where k:v is file_name:dataframe of data in the file
    '''
    data = {}
    for file in os.listdir(folder_path):
        if file.endswith('.csv') and file != schema_file:
            table_name = file.replace('.csv', '')
            file_path = os.path.join(folder_path, file)
            data[table_name] = pd.read_csv(file_path)
    return data
