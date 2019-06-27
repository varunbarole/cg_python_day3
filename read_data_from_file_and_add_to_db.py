import pymysql

db = pymysql.connect(host="localhost",port=3306,user="root",password ="mysql12345", database="cg1")

cursor = db.cursor()

FILEPATH = "C:\\Users\\vb1017665\PycharmProjects\learning\python_training_day-3\\realestate.csv"

print (FILEPATH)

fobj = open("C:\\Users\\vb1017665\PycharmProjects\learning\python_training_day-3\\realestate.csv","r")
for line in fobj:
    line = line.strip()
    output = line.split(",")
    query = "insert into realestate values('{}','{}',{},'{}')".format(output[0],output[1],output[2],output[3])
    cursor.execute(query)

db.commit()

db.close()