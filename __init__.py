__author__ = 'Rashed'
#!/usr/bin/python
import psycopg2
import sys
import pprint

def main():
	conn_string = "host='localhost' dbname='movie_db' user='postgres' password='5510'"
	# print the connection string we will use to connect
	print("Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()


if __name__ == "__main__":
	main()