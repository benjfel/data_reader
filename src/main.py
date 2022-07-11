# THIS FILE IS FOR TESTING PURPOSES
import data_reader as dr
import data_access as da

# suppliers = dr.read_csv('suppliers.csv',',',True)
suppliers = dr.read_json('suppliers.json')
# suppliers = dr.read_xml('suppliers.xml')

secrets = dr.read_json('secrets.json')

conn = da.connect(driver=secrets['Driver'],
                  server=secrets['Server'],
                  database=secrets['Database'],
                  trusted_connection=True,
                  username='',
                  password='')

cursor = conn.cursor()

count = 0
for s in suppliers:
    count += cursor.execute('INSERT INTO Production.Suppliers VALUES(?,?,?,?,?,?,?,?,?,?)',
                            s['name'],
                            s['contact_name'],
                            s['contact_title'],
                            s['address'],
                            s['city'],
                            s['region'],
                            s['postal_code'],
                            s['country'],
                            s['phone'],
                            s['fax']).rowcount

conn.commit()

print('Rows inserted: ' + str(count))