import pyodbc 

def connect(driver, server, database, trusted_connection = True, username = '', password = ''):
    
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection};UID={username};PWD={password}'

    connection = pyodbc.connect(connection_string)

    return connection.cursor()