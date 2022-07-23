# FOR TESTING PURPOSES
import data_reader as dr
import data_access as da

params = dr.read_json('suppliers.json')

conn = da.connect(driver='',
                  server='',
                  database='',
                  trusted_connection=True,
                  username='',
                  password='')

statement = """
    INSERT INTO Production.Suppliers VALUES
    (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
    )
"""

row_count = 0
for p in params:
    row_count += conn.execute(statement,
                              p['name'],
                              p['contact_name'],
                              p['contact_title'],
                              p['address'],
                              p['city'],
                              p['region'],
                              p['postal_code'],
                              p['country'],
                              p['phone'],
                              p['fax']).rowcount

print(str(row_count))