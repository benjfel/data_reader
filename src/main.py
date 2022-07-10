import data_reader as dr
import data_access as da

# suppliers = dr.read_csv('suppliers.csv',',',True)

suppliers = dr.read_xml('suppliers.xml')

print(suppliers)

# secrets = dr.read_json('secrets.json')

# conn = da.connect(secrets['Driver'],
#                   secrets['Server'],
#                   secrets['Database'],
#                   True)

# cursor = conn.cursor()

# count = 0
# for s in suppliers:
#     count += cursor.execute('INSERT INTO Production.Suppliers VALUES(?,?,?,?,?,?,?,?,?,?)',
#                             s[1],
#                             s[2],
#                             s[3],
#                             s[4],
#                             s[5],
#                             s[6],
#                             s[7],
#                             s[8],
#                             s[9],
#                             None).rowcount

# conn.commit()

# print('Rows inserted: ' + str(count))