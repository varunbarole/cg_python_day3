import pymysql

db = pymysql.connect(host="localhost",port=3306,user="root",password="mysql12345")

print (db)