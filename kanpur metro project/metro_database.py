import mysql.connector
nayan=mysql.connector.connect(host="localhost",user="root",password="nayanmishra",database="enquiryportal")
cur=nayan.cursor()
#cur.execute("create database enquiryportal")
cur.execute("create table data1(station_number1 varchar(500),station_number2 varchar(300))")
nayan.commit()
