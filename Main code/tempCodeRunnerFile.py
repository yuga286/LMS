# from flask import Flask,render_template,request
# import mysql.connector 

# app = Flask(__name__)

# try:
#     yu = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         database="new1",
#         password="Niku@Bro@123",
#         port=8080  # Specify the port if it's different from the default 3306
#     )
#     cursor = yu.cursor()
#     print("Connected to the database")
# except mysql.connector.Error as err:
#     print("Error connecting to database:", err)
    
    
# @app.route('/', methods=['GET','POST'])
# def index():
  
#     return render_template('demo.html')
    
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect
import mysql.connector 

app = Flask(__name__, template_folder = r'F:\vs workspace\basic\python\python pro LMS\templates')

try:
    yu = mysql.connector.connect(
        host="localhost",
        user="root",
        database="new1",
        password="Niku@Bro@123",
        port=8080 
    )
    cursor = yu.cursor()
    print("Connected to the database")
except mysql.connector.Error as err:
    print("Error connecting to database:", err)

@app.route('/demo', methods=['GET','POST'])
def index():
    return render_template('/demo.html')

if __name__ == '__main__':
    app.run(debug=True)
