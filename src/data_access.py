import pyodbc 

def connect(driver, server, database, trusted_connection = True, username='', password=''):
    
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection};UID={username};PWD={password}'

    return pyodbc.connect(connection_string)


# write dml functions
# secrets = dr.read_json('secrets.json')

# conn = da.connect(driver=secrets['Driver'],
#                   server=secrets['Server'],
#                   database=secrets['Database'],
#                   trusted_connection=True,
#                   username='',
#                   password='')

# cursor = conn.cursor()

# count = 0
# for s in suppliers:
#     count += cursor.execute('INSERT INTO Production.Suppliers VALUES(?,?,?,?,?,?,?,?,?,?)',
#                             s['name'],
#                             s['contact_name'],
#                             s['contact_title'],
#                             s['address'],
#                             s['city'],
#                             s['region'],
#                             s['postal_code'],
#                             s['country'],
#                             s['phone'],
#                             s['fax']).rowcount

# conn.commit()

# print('Rows inserted: ' + str(count))