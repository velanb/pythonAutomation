import mysql.connector
from mysql.connector import errorcode
import sys
import csv


# This function is to connect to the mySql database
def connect_db(db_username, db_password, db_host, db_name):
  try:
    cnx = mysql.connector.connect(host=db_host, user=db_username, password=db_password, database=db_name)
    return cnx
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cnx.close()



#exec queries on the database and export them to csv
#@param - db_config { db_username: "username", db_password: "password", db_host:"host", db_name:"db name"}
#@param - query string - The actual query
def exec_query_db(query_string, db_config, file_name):
  # connect to db first
  cursor = connect_db(db_config['db_username'], db_config['db_password'], db_config['db_host'], db_config['db_name'])
  cursor.execute(query_string)
  myresult = cursor.fetchall()
  c = csv.writer(open(file_name, 'wb'))
  for x in myresult:
    c.writerow(x)



# read CSV using pandas as a dataframe


#Do the math



