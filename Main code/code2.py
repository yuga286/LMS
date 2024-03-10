import mysql.connector
my=mysql.connector.connect(host="localhost",user="root",password="Niku@Bro@123",database="new1",port="8080")

First_Name = input("Enter Book name: ")
Last_Name= input("Enter Book Author: ")
# Insert data into the MySQL database
cursor = my.cursor()
query = "INSERT INTO Student_Data (First_Name,Last_Name) VALUES ( %s, %s)"
values = (First_Name,Last_Name)
cursor.execute(query, values)
my.commit()

