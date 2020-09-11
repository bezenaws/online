import csv
import MySQLdb
# open the connection to the MySQL server.
# using MySQLdb
mydb = MySQLdb.connect(host='igor.gold.ac.uk', user='co304so', passwd='*********', db='co304so_LondonCrime')
cursor = mydb.cursor()
csv_data = csv.reader(file('1.csv'))
# execute and insert the csv into the database.
for row in csv_data:
	cursor.execute('INSERT INTO AprilNov2013(Date,Westminster,HACKNEY,Tower_Hamlets)''VALUES(%s, %s, %s, %s)',row)
	print row
#close the connection to the database.
mydb.commit()
cursor.close()
print "CSV has been imported into the database"
