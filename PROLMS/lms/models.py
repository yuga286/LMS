from django.db import models

class Info(models.Model):
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    User_Name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=100)
    Image=models.ImageField(upload_to='lmss/', blank=True, null=True, default='default_image_path.jpg')
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Student_Data'

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    Book_ID = models.AutoField(primary_key=True)
    Book_Name = models.CharField(max_length=256, blank=False)
    Book_Image=models.ImageField(upload_to='lmsss/', blank=True, null=True, default='default_image_path.jpg')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    Book_Count=models.IntegerField()
    Publication_Year = models.DateTimeField(blank=True, null=True)
    Publisher = models.CharField(max_length=100, blank=True)
    
    class Meta:
        db_table='Book_Data'


from django.db import models

class AdminData(models.Model):
    Admin_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=100, blank=False)
    Middle_Name = models.CharField(max_length=100, blank=True, null=True)
    Last_Name = models.CharField(max_length=100, blank=False)
    User_Name = models.CharField(max_length=100, blank=False)
    Contact_Number = models.CharField(max_length=100, blank=True, null=True)
    Image = models.ImageField(upload_to='admin_images/', blank=True, null=True, default='default_image_path.jpg')
    Email = models.EmailField(blank=False, unique=True)
    Password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.User_Name
    
    class Meta:
        db_table='Admin_Data'