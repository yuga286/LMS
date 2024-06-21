from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
# from django.contrib.auth.models import StudentData
# from service.models import StudentData
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.db import models
from lms.models import Info
from lms.models import Book
from django.urls import reverse

def dhome(reuest):
    return HttpResponseRedirect('home')

def superior(request):
    return render(request,'superior.html')

def home(request):
    return render(request, 'home.html')

def student_login(request):
    # Your login view logic goes here
    return render(request, "student_login.html") 

def student_dashboard(request):
    return render(request, "student_dashboard.html")

def registation(request):
    # Your login view logic goes here
    return render(request, "registation.html") 

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")

def admin_login(request):
    return render(request,"admin_login.html")

def admin_registation(request):
    return render(request,"admin_registation.html")

def borrow(request):
    return render(request,"borrow.html")

def dashboard_info(request):
    return render(request,"dashboard_info.html")

def dashboard(request):
    return render(request,"dashboard.html")

def enter(request):
    return render(request,"enter.html")

def exit(request):
    return render(request,"exit.html")

def fetch_result(request):
    return render(request,"fetch_result.html")

def fetch(request):
    return render(request,"fetch.html")

def submit(request):
    if request.method == 'POST':
        # Get the data from the form
        First_Name = request.POST.get('First_Name')
        Middle_Name = request.POST.get('Middle_Name')
        Last_Name = request.POST.get('Last_Name')
        User_Name = request.POST.get('User_Name') 
        Contact_Number = request.POST.get('Contact_Number') 
        email = request.POST.get('email') 
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        
        if password != confirm_password:
            messages.error(request, "Password and confirm password do not match.")
            return render(request, "home.html")
        
        student=Info(
        First_Name=First_Name,
        Middle_Name=Middle_Name,
        Last_Name=Last_Name,
        User_Name=User_Name,
        Contact_Number=Contact_Number,
        email=email,
        password=password
        )
        student.save()
        # messages.success(request, "Data saved to database successfully.")
        return render(request, "home.html")
        
    return render(request,"home.html")        


# from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == 'POST':
        username = request.POST.get('User_Name')
        password = request.POST.get('password')
        
        # Check if user exists in the Info table
        try:
            user_info = Info.objects.get(User_Name=username)
        except Info.DoesNotExist:
            return render(request, 'student_login.html', {'error': 'user does not exist'})
        
        # Check if the provided password matches the stored password
        if (password==user_info.password):
            
            # Store user_info object in session
            request.session['user_info'] = {
                'First_Name': user_info.First_Name,
                'Middle_Name': user_info.Middle_Name,
                'Last_Name': user_info.Last_Name,
                "User_Name": user_info.User_Name,
                # Add more fields as needed
            }
            # Redirect to dashboard or desired page
            return render(request, 'dashboard.html', {'user_info': user_info})
        else:
            # Return an 'invalid login' error message
            return render(request, 'student_login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'student_login.html')


def fetch(request):
    if request.method == 'POST':
        search_term = request.POST.get('bookname', '')# Assuming the search term comes from a form input with the name 'search_term'
        results = Book.objects.filter(Book_Name__icontains=search_term)
        return render(request, 'fetch_result.html', {'results': results, 'user_info': request.session.get('user_info')})
    else:
        # Handle other HTTP methods (GET, etc.) as needed
        return render(request, 'home.html')
    

# from django.shortcuts import render
# from service.models import BorrowForm  # Import your BorrowForm class

def borrow(request):
    error = None
    success = None

    if request.method == 'POST':
        # No form instantiation here
        if request.POST.get('bookname') and request.POST.get('days'):
            book_name = request.POST['bookname']
            days = request.POST['days']
            # Perform further processing if needed
            success = 'Book "{}" added successfully for {} days.'.format(book_name, days)
        else:
            error = 'Please provide book name and days.'

    # No form instantiation for GET requests

    return render(request, 'borrow.html', {'error': error, 'success': success})
