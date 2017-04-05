# Insert-data-into-PostgreSQL-from-CSV-file-using-python-3


## Introduction:
Our aim is to insert data into PostgreSQL database from defferent CSV file.

## Prerequisites
To do this work we have to do first install python on our machine also have setup PostgreSQL

## Running the tests
 __init__.py in this file we are creating connection with PostgreSQL database also we are creating database in this page name "movie_db"

table_create.py in this python file we are creating tables on database.We are keeping our PostgreSQL queries into a dictionary named"TABLES={}"
By using for loop we are executing the queries into database for creating table.

insert_movies.py in this python file we are creating 4 function for inserting data on 4 different  table from 4 different CSV file.In
the begining of function we are opening the CSV file.
Then using forloop we read the data from csv file and then inserting the data by query into database.
 
## After inserting data the database screenshot
1. ![Screenshot of full database](https://github.com/sabiul/Insert-data-into-PostgreSQL-from-CSV-file-using-python-3/blob/master/screenshot/home.png "Screenshot of full database")

2. ![Movies Table](https://github.com/sabiul/Insert-data-into-PostgreSQL-from-CSV-file-using-python-3/blob/master/screenshot/scrn-.png "Movies Table")
