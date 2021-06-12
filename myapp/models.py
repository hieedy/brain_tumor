from django.db import models
from django.utils import timezone
# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=100)
    email  = models.EmailField()
    message = models.CharField(max_length=500)
    subject= models.CharField(max_length=500)

class blogs(models.Model):
    authorname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.TextField()
    postdate=models.DateField(null=True)
    image = models.ImageField(null=True, upload_to="blog/")

 
class Register(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email  = models.EmailField()
    password=models.CharField(max_length=20)
    
    contactno=models.CharField(max_length=10)
    address=models.CharField(max_length=50)  

class diseases(models.Model):  
    name=models.CharField(max_length=100)   
    description=models.TextField(null=True) 
    url=models.URLField()      

class clinics(models.Model):
    name=models.CharField(max_length=100) 
    city=models.CharField(max_length=100)
    state =models.CharField(max_length=100)
    full_address =models.CharField(max_length=100)
    start_time=models.TimeField()
    closing_time=models.TimeField() 

    def __str__(self):
        return self.name

class patient(models.Model):
        
    Name=models.CharField(max_length=100)
    password=models.CharField(max_length=15)
    email=models.EmailField()
    

    gender=models.CharField(max_length=100, null= True) 
    
    contact=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100, null=True)
    state=models.CharField(max_length=100, null=True)
    pincode=models.IntegerField(null=True)
    dob=models.DateField(null=True)
    bloodgroup =models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    profile_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.Name
    
class hospital(models.Model):    
    
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField() 
    location=models.TextField(null=True)
    description=models.TextField(null=True)
    address=models.CharField(max_length=100)
    opening_hrs=models.CharField(max_length=20)
    specialization=models.CharField(max_length=30)
    profile_image=models.ImageField(null=True, blank=True)
    contact=models.IntegerField(null=True)

    
    def __str__(self):
        return self.name

class doctor(models.Model):
    
    name=models.CharField(max_length=100) 
    password=models.CharField(max_length=15)
    Email=models.EmailField()
    gender=models.CharField(max_length=100)   
    phone=models.IntegerField() 
    experience_yrs=models.FloatField(max_length=10) 
    pincode=models.IntegerField() 
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)
    clinic_id = models.ForeignKey(clinics, on_delete=models.CASCADE, null=True, blank =True)
    hospital_id = models.ForeignKey(hospital, on_delete=models.CASCADE, null=True, blank =True)
    profile_image = models.ImageField(null=True, blank = True)
    specialization= models.CharField(max_length=30)
    dob = models.DateField()

    def __str__(self):
        return self.name+"-->"+self.Email


class labs(models.Model):
    name=models.CharField(max_length=100)  
    city=models.CharField(max_length=100)  
    state=models.CharField(max_length=100)   
    full_address=models.CharField(max_length=100)   
    start_time=models.IntegerField()
    closing_time=models.IntegerField() 
    profile_image=models.ImageField(null=True, blank=True)
    contact=models.IntegerField(null=True)
    location=models.TextField(null=True)

    def __str__(self):
        return self.name




class appointment_table(models.Model):
    patient_id=models.ForeignKey(patient,on_delete=models.CASCADE,null=True)
    doctor_id=models.ForeignKey(doctor, on_delete=models.CASCADE,null=True)
    # disease_id  = models.ForeignKey(diseases, on_delete = models.CASCADE)
    Date=models.DateField()
    Time=models.TimeField()	
    apply_date=models.DateField()
    Appointment_Status = (
        ('A', 'Approved'),
        ('NA', 'Not Approved'),
        ('P', 'Pending')
    )
    status = models.CharField(max_length=2, choices=Appointment_Status, default='P')
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField()


class Message(models.Model):
	From=models.EmailField(max_length=100)
	to=models.EmailField(max_length=100)
	Date=models.DateField()
	Time=models.TimeField()
	Message=models.CharField(max_length=100)
	Attachment=models.FileField(null=True, blank=True)    
	appointment_id = models.ForeignKey(appointment_table, on_delete=models.CASCADE)


class chat_table(models.Model):
    patient_id=models.ForeignKey(patient,on_delete=models.CASCADE,null=True)
    doctor_id=models.ForeignKey(doctor, on_delete=models.CASCADE,null=True)
    # disease_id  = models.ForeignKey(diseases, on_delete = models.CASCADE)
    Time=models.TimeField()	
    days_left=models.IntegerField()
    Chat_Status = (
        ('A', 'Active'),
        ('NA', 'Not Active'),
    )
    status = models.CharField(max_length=2, choices=Chat_Status, default='A')
    is_active = models.BooleanField()    
    

class helpandsupport(models.Model):
    subject=models.CharField(max_length=100, null =True, blank = True)
    message=models.TextField(max_length=100, null =True, blank = True)
    user_email = models.EmailField()



# 	clinic_id = models.ForeignKey()
# class Doctor:
# 	registeration_no (pk)
# 	name
# 	email
# 	gender
# 	phone
# 	experience(in yrs)
# 	address
# 	pincode
# 	city
# 	state
# 	no._of_surgeries
# 	qualification_id = model.ForeignKey(Qualification, on_delete = models.CASCADE)
# disease_id=models.ForeignKey(diseases, on_delete=models.CASCADE,null=True)
# 	



# clinics:
# name

# city
# state
# full_address
# starting_time
# closing_time
# Hospitals:
# name
# full_address
# city
# state
# pincode
# no._of_beds
# no.of_rooms

