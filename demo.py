# import execjs
from flask import Flask, render_template,request,redirect, url_for,jsonify,session
from datetime import datetime
import mysql.connector
from email_validator import validate_email, EmailNotValidError 

app = Flask(__name__,static_url_path='/static')
app.secret_key = 'books' 

try:
    con={
        "host": "localhost",
        "user": "root",
        "database": "new1",
        "password": "Niku@Bro@123",
        "port": 8080
    }
    yu = mysql.connector.connect(**con)
    cursor = yu.cursor()
    print("Connected to the database")
except mysql.connector.Error as err:
    print("Error connecting to database:", err)

@app.route('/')
def index():
    return render_template('registation.html') 

@app.route('/home')
def home():
    return render_template('home.html')




@app.route('/submit', methods=['POST'])
def submit():
    
    if request.method == 'POST':
        # Get the username from the form
        First_Name = request.form.get('First_Name')
        Middle_Name = request.form.get('Middle_Name')
        Last_Name = request.form.get('Last_Name')
        User_Name=request.form.get('User_Name') 
        Contact_Number=request.form.get('Contact_Number') 
        email=request.form.get('email') 
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')
        
        
        try:
            v = validate_email(email)
            email = v.email
        except EmailNotValidError as e:
            return render_template('registation.html', condition=True, error_message=f"Invalid email address: {e}")

        
        if password != confirm_password:
            return render_template('registation.html',condition=True)
        else:
            try:
                sql = "INSERT INTO Student_Data (First_Name,Middle_Name,Last_Name,password,User_Name,Contact_Number,email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                values = (First_Name,Middle_Name,Last_Name,password,User_Name,Contact_Number,email)
                cursor.execute(sql, values)
                yu.commit()
                return "Username submitted successfully!"
            except mysql.connector.Error as err:
                yu.rollback()
                return f"Error inserting data into the database: {err}"
            finally:
                cursor.close()
                yu.close()
                


@app.route('/dashboard/<string:User_Name>')
def get_user(User_Name):
    connection = mysql.connector.connect(**con)
    cursor = connection.cursor(dictionary=True)

    query = "SELECT ID, First_Name, Middle_Name, Last_Name, List_Of_issued_Book, Number_of_issued_Book, password, User_Name FROM Student_Data WHERE User_Name = %s"
    cursor.execute(query, (User_Name,))
    user = cursor.fetchone()


    cursor.close()
    connection.close()

    if user:
        return user
    else:
        return jsonify({"error": "data not found"}), 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        User_Name = request.form.get('User_Name')
        password = request.form.get('password')
        if authenticate_user(User_Name, password):
            # Assuming 'get_user_data' is a function to retrieve user data from the database
            user_data = get_user(User_Name)
            if user_data:
                # Store user_data in the session
                session['user_data'] = user_data
                return render_template('dashboard.html')
            else:
                return render_template('login.html', error='User data not found')

        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')


@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    return render_template('student_dashboard.html')
    
def authenticate_user(User_Name, password):
    try:
        # Establish a database connection
        connection = mysql.connector.connect(**con)
        cursor = yu.cursor()

        # Query to check login credentials
        query = "SELECT * FROM Student_Data WHERE User_Name = %s AND password = %s"
        cursor.execute(query, (User_Name, password))

        # Fetch the result
        user = cursor.fetchone()
        if user:
            # User authenticated
            return True
        else:
            # Invalid credentials
            return False
    finally:
        # Close the database connection
        cursor.close()
        connection.close()


@app.route('/student_dashboard', methods=['GET','POST'])
def student_dashboard():
    if 'user_data' in session:
        user_data = session['user_data']
        return render_template('student_dashboard.html', user_data=user_data)
    else:
        return ("user not found")




# fetch method



@app.route('/fetch/<string:bookname>')
def get_book_data(bookname):
    connection = mysql.connector.connect(**con)
    cursor = connection.cursor(dictionary=True)

    query = "SELECT Book_ID, Book_Name, Book_Count, Author, Publication_Year, Publisher FROM Book_Data WHERE Book_Name = %s"
    cursor.execute(query, (bookname,))
    book_data = cursor.fetchone()

    cursor.close()
    connection.close()
    session['book_data'] = book_data

    return book_data


@app.route('/fetch', methods=['GET','POST'])
def fetch():
    if request.method == 'POST':
        book_name = request.form.get('bookname')
        if not book_name:
            return render_template('fetch.html', error_message='Please provide a book name')
        
        book_data = get_book_data(book_name)
        
        if book_data:
            return render_template('fetch_result.html', book_data=book_data)
        else:
            return render_template('fetch.html', error_message='Book not found in the database')

    return render_template('fetch.html')

@app.route('/fetch_result', methods=['GET','POST'])
def fetch_result():
    
    # Retrieve the book data from the Flask session
    book_data = session.get('book_data')
    if book_data:
        return render_template('fetch_result.html', book_data=book_data)
    else:
        return render_template('fetch.html', error_message='Book not found in the session')



# borrow
@app.route('/borrow', methods=['GET','POST'])
def borrow():
    # book_name = request.form.get('bookname')
    # days = request.form.get('days')
    
    # indatetime = datetime.now()
    # sql = "INSERT INTO Student_Data (First_Name,Middle_Name,Last_Name,password,User_Name,Contact_Number,email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    
    

    
    return render_template('borrow.html')











@app.route('/admin_registation', methods=['GET','POST'])
def admin_registation():
    
    if request.method == 'POST':
        # Get the username from the form
        First_Name = request.form.get('First_Name')
        Last_Name = request.form.get('Last_Name')
        User_Name=request.form.get('User_Name') 
        Contact_Number=request.form.get('Contact_Number') 
        email=request.form.get('email') 
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')
        
        
        try:
            v = validate_email(email)
            email = v.email
        except EmailNotValidError as e:
            return render_template('admin_registation.html', condition=True, error_message=f"Invalid email address: {e}")

        
        if password != confirm_password:
            return render_template('admin_registation.html',condition=True)
        else:
            try:
                sql = "INSERT INTO Admin_Data (Admin_First_Name,Admin_Last_Name,Admin_password,Admin_User_Name,Contact_Number,Admin_email) VALUES (%s,%s,%s,%s,%s,%s)"
                values = (First_Name,Last_Name,password,User_Name,Contact_Number,email)
                cursor.execute(sql, values)
                yu.commit()
                return "Username submitted successfully!"
            except mysql.connector.Error as err:
                yu.rollback()
                return f"Error inserting data into the database: {err}"
            finally:
                cursor.close()
                yu.close()
    return render_template('admin_registation.html')

@app.route('/admin_dashboard/<string:User_Name>')
def admin_get_user(User_Name):
    connection = mysql.connector.connect(**con)
    cursor = connection.cursor(dictionary=True)

    query = "SELECT Admin_ID, Admin_First_Name, Admin_Last_Name, Admin_email, Admin_User_Name, Admin_Password, Contact_Number FROM Admin_Data WHERE Admin_User_Name = %s"
    cursor.execute(query, (User_Name,))
    user = cursor.fetchone()
    print(user)

    cursor.close()
    connection.close()

    if user:
        return user
    else:
        return jsonify({"error": "User not found"}), 404


def admin_authenticate_user(User_Name, password):
    try:
        # Establish a database connection
        connection = mysql.connector.connect(**con)
        cursor = yu.cursor()

        # Query to check login credentials
        query = "SELECT * FROM Admin_Data WHERE Admin_User_Name = %s AND Admin_password = %s"
        cursor.execute(query, (User_Name, password))

        # Fetch the result
        user = cursor.fetchone()
        if user:
            # User authenticated
            return True
        else:
            # Invalid credentials
            return False
    finally:
        # Close the database connection
        cursor.close()
        connection.close()

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        User_Name = request.form.get('User_Name')
        password = request.form.get('password')
        if admin_authenticate_user(User_Name, password):
            # Assuming 'get_user_data' is a function to retrieve user data from the database
            user_data = admin_get_user(User_Name)
            if user_data:
                # Store user_data in the session
                session['user_data'] = user_data
                return render_template('admin_dashboard.html')
            else:
                return render_template('admin_login.html', error='User data not found')

        else:
            return render_template('admin_login.html', error='Invalid credentials')

    return render_template('admin_login.html')



@app.route('/enter_book',methods=['GET','POST'])
def enter():
    if request.method == 'POST':
        # Get the username from the form
        
        BookName=request.form.get('bookName')
        Author=request.form.get('bookAuthor')
        PublicationYear=request.form.get('Year')
        Publication=request.form.get('Publication')
        count=int(request.form.get('count'))
        
        try:
            cursor = yu.cursor()
            check_sql = "SELECT * FROM Book_Data WHERE Book_Name = %s"
            cursor.execute(check_sql, (BookName,))
            existing_book = cursor.fetchone()
            

            if existing_book:
                current_datetime = datetime.now()
                entertime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                c = list(existing_book)
                existing_entry_count = c[2]
                countE = existing_entry_count + count
                bookid=c[0]
                
                sql = "UPDATE Book_Data SET Book_Count = %s WHERE Book_Name = %s"
                values = (countE,BookName)
                insert_sql = "INSERT INTO Book_Entries (Book_ID,Book_Name, Entry_Time, Entry_Count) VALUES (%s, %s, %s, %s)"
                insert_values = (bookid,BookName,entertime,count)
                cursor.execute(sql, values)
                cursor.execute(insert_sql,insert_values)
                yu.commit()
                return "Book Data submitted successfully!"
            else:
                sql = "INSERT INTO Book_Data (Book_Name,Author,Publication_Year,publisher,Book_Count) VALUES (%s,%s,%s,%s,%s)"
                values = (BookName,Author,PublicationYear,Publication,count)
                cursor.execute(sql, values)
                yu.commit()
                return "Book Data submitted successfully!"
            

            
        except mysql.connector.Error as err:
            yu.rollback()
            return f"Error inserting data into the database: {err}"
        finally:
            cursor.close()
            yu.close()
    return render_template('enter.html')
@app.route('/exit_book',methods=['GET','POST'])
def exit():
    if request.method == 'POST':
        # Get the username from the form
        
        BookName=request.form.get('bookName')
        count=int(request.form.get('count'))
        
        try:
            cursor = yu.cursor()
            check_sql = "SELECT * FROM Book_Data WHERE Book_Name = %s"
            cursor.execute(check_sql, (BookName,))
            existing_book = cursor.fetchone()

            if existing_book:
                current_datetime = datetime.now()
                exittime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                c = list(existing_book)
                existing_count = c[2]
                countE = existing_count - count
                bookid=c[0]

                sql = "UPDATE Book_Data SET Book_Count = %s WHERE Book_Name = %s"
                values = (countE,BookName)
                insert_sql = "INSERT INTO Book_Entries (Book_ID,Book_Name, Exit_Time, Exit_Count) VALUES (%s, %s, %s, %s)"
                insert_values = (bookid,BookName,exittime,count)
                cursor.execute(sql, values)
                cursor.execute(insert_sql,insert_values)
                
                yu.commit()
                return "Book Data submitted successfully!"
            else:
                return "Book Data is not available"
        except mysql.connector.Error as err:
            yu.rollback()
            return f"Error inserting data into the database: {err}"
        finally:
            cursor.close()
            yu.close()
    return render_template('exit.html')
@app.route('/admin_dashboard', methods=['GET','POST'])
def admin_dashboard():
    if 'user_data' in session:
        user_data = session['user_data']
        return render_template('dashboard_info.html', user_data=user_data)
    else:
        return redirect(url_for('admin_login'))

                
if __name__ == '__main__':
    app.run(debug=True)