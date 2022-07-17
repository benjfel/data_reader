# THIS FILE IS FOR TESTING PURPOSES
import data_reader as dr
import data_access as da

suppliers = dr.read_excel(r'C:\repos\data_reader\src\suppliers.xls', True)

print(suppliers)

# secrets = dr.read_json('secrets.json')

# conn = da.connect(driver=secrets[1]['Driver'],
#                   server=secrets[1]['Server'],
#                   database=secrets[1]['Database'],
#                   trusted_connection=True,
#                   username='',
#                   password='')

# cursor = conn.cursor()

# command = """
#     SELECT *
#     FROM 
# """

# cursor.execute(command)

# results = cursor.fetchall() 
# for r in results:
#     print(r)