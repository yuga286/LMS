# import json
# class Main:
#         def __init__(self):
#             print("press 1 if you are a student")
#             print("press 2 if you are an admin")
#             user=input("Enter the number of your choice: ")
#             if(user=="1"):
#                 print("welcome Student")
#                 print("press 1 if you want to login")
#                 print("press 2 if you want to sign up")
#                 endUser=input("Enter the number of your choice: ")
#                 if(endUser==1):
#                     self.enterStudent()
#                 else:
#                     self.createStudent()
#             else:
#                 print("welcome Admin")
#                 print("press 1 if you want to login")
#                 print("press 2 if you want to sign up")
#                 adminUser=input("Enter the number of your choice: ")
#                 if(adminUser==1):
#                     self.enterAdmin()
#                 else:
#                     self.createAdmin()      
                    
#         def createAdmin(self):
#             self.admin_name = input("Enter Admin Name: ")
#             self.admin_email = input("Enter Admin Email: ")
#             self.admin_password = input("Enter Admin Password: ")
            
#             with open("F:/vs workspace/basic/python/python pro LMS/data/admin.json","r") as file_admin:
#                 e_Admin=json.load(file_admin)
            
            
#             data = {
#                 "Admin_name": self.admin_name,
#                 "Admin_email": self.admin_email,
#                 "Admin_password": self.admin_password
#                 }
#             e_Admin.append(data)
            
#             with open("F:/vs workspace/basic/python/python pro LMS/data/admin.json", "w") as fileA:
#                 json.dump(e_Admin,fileA,indent=4)
                
#             self.enterAdmin(self)
            
            
#         @staticmethod
#         def enterAdmin(self):
            
#             adminName = input("Enter Admin Name: ")
#             adminEmail = input("Enter Admin Email: ")
#             adminPassword = input("Enter Admin Password:")

#             self.admin_name = adminName
#             self.admin_email = adminEmail
#             self.admin_password = adminPassword
#             self.adminProfile(self)
            
#         def createStudent(self):
#             self.student_name = input("Enter Student Name: ")
#             self.student_email = input("Enter Student Email: ")
#             self.student_password = input("Enter Student Password: ")
            
#             with open("F:/vs workspace/basic/python/python pro LMS/data/StudentData.json","r") as file_Student:
#                 S_Admin=json.load(file_Student)
            
#             info = {
#                 "Student_name": self.student_name,
#                 "Student_email": self.student_email,
#                 "Student_password": self.student_password
#                 }
#             S_Admin.append(info)
            
#             with open("F:/vs workspace/basic/python/python pro LMS/data/StudentData.json", "w") as files:
#                 json.dump(S_Admin,files,indent=4)
                
#             self.enterStudent(self)
            
#         @staticmethod  
#         def enterStudent(self):
            
#             studentName=input("Enter student name:")
#             studentEmail=input("Enter email:")
#             studentPassword=input("Enter password:")
            
#             self.student_name = studentName
#             self.student_email = studentEmail
#             self.student_password = studentPassword
#             self.studentId()
            
#         def studentId(self):
#             bookName=input("Enter Book name:")
#             bookAuthor=input("Enter Book Author:")
#             bookpublishedyear=input("Enter Book Published Year:")
            
#             self.book_Name =bookName
#             self.book_Author =bookAuthor
#             self.book_published_year =bookpublishedyear
            
            
            
#             with open('/python/python pro LMS/data/BookData.json', 'r') as f:
#                 books = json.load(f)
                
#             print(len(books))

            
            
            
            
            
#         # def adminProfile(self):
            
            
# obj=Main()    


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





# host="localhost"
# conn={
#     'user':'root',
#     'password':'Niku@Bro@123',
# 'database':'Student_Data'
# }
# port="3306"

# def Main():
    # try:
import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="Niku@Bro@123",database="Student_Data")
# connection = mysql.connector.connect(**conn)
        
        # if connection.is_connected():
        #     print("Connected to MySQL")
    
# cursor = connection.cursor()
        
        # cursor.execute("SELECT * FROM Student_Data")
        # rows = cursor.fetchall()

        # for row in rows:
        #         print(row)
                
# cursor.close()
        
# connection.close()
# print("Connection closed")

# print("Data fetched successfully")

    
    # except mysql.connector.Error as err:
    #     print(f"Error: {err}")
        
# Main()