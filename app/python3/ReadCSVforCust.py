import csv
import pymysql
# open the connection to the MySQL server.
# using MySQLdb
conn = pymysql.connect(host='localhost', user='admin', passwd=None, db='test')
cur = conn.cursor()
csv_data = csv.reader(open('1.csv'))
# execute and insert the csv into the database.
for row in csv_data:
	cur.execute('INSERT INTO clients(name,contact,title,address)''VALUES(%s, %s, %s, %s)',row)
	print (row)
#close the connection to the database.
conn.commit()
cur.close()
print ("CSV has been imported into the database")
