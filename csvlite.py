#!/usr/bin/env python3

import sys
import csv
import sqlite3

def sql_to_csv(DATABASE_NAME, TABLE_NAME, CSV_OUTPUT)
	if (CSV_OUTPUT == ""):
		CSV_OUTPUT = "output.csv"
	conn = sqlite3.connect(DATABASE_NAME)
	cur = conn.cursor()
	data = cur.execute("SELECT * FROM {0}".format(TABLE_NAME))

	with open(CSV_OUTPUT, 'wb') as f:
	    writer = csv.writer(f)
	    writer.writerows(data)

	conn.close()

def csv_to_sql(DATABASE_NAME, TABLE_NAME, CSV_FILENAME):
	if (DATABASE_NAME == ""):
		DATABASE_NAME = "TEST.db"

	if (TABLE_NAME == ""):
		TABLE_NAME = "DEFAULT_TABLE"

	if (CSV_FILENAME == ""):
		print ("enter a real CSV filename")
		sys.exit()

	my_file = open(CSV_FILENAME, 'r')
	reader = csv.reader(my_file, delimiter=',')

	date = datetime.datetime.now().strftime("%Y-%M-%d")

	con = lite.connect(DATABASE_NAME, isolation_level = 'exclusive')
	cur  = con.cursor()

	table_names = set(row[1] for row in reader)
	my_file.seek(0)

	for name in table_names:
	     cur.execute("CREATE TABLE IF NOT EXISTS [%s] (Date TEXT, Position INT)" % item_name)

	for row in reader:
	    position = row[0]
	    item_name = row[1]

	    cur.execute("INSERT INTO [%s] VALUES(?, ?)" % item_name, (date, position))

	con.commit()