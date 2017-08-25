from psycopg2 import connect
import sys
import csv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT,

con = connect(dbname ='bridge', user='dimka', password='qwe123')

# dbname = "dbtest"

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('CREATE TABLE data (id int, html text, link_id int, parent_id int, PRIMARY KEY(id))')
cur.execute('CREATE TABLE data_links (category_id int)')
print('database is created')
cur.close()
con.close()