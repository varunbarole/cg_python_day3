import pymysql

db = pymysql.connect(host="localhost",port=3306,user="root",password ="mysql12345")

cursor = db.cursor()

query = "create database cg1"

cursor.execute(query)

db.close()