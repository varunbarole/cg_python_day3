import pymysql

db = pymysql.connect(host="localhost",port=3306,user="root",password ="mysql12345", database="cg1")

cursor = db.cursor()

query = "create table numbers (number int);"

cursor.execute(query)

db.close()