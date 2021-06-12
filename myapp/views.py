from django.shortcuts import render, redirect

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse

from myapp.models import contact, helpandsupport, labs
from myapp.models import Register
from myapp.models import patient
from myapp.models import doctor
from myapp.models import hospital
from myapp.models import blogs
from myapp.models import diseases , appointment_table
from datetime import date
from datetime import datetime
from myapp.models import labs
from myapp.models import Message
from myapp.models import chat_table




# Create your views here.
def logout(request):
    if not  request.session.has_key('email'):
        return redirect('/login')
    else:
        del request.session['email']

    return redirect('/login')    
    
def form(request):
    return render(request,'abc.html',{})

def register(request):
    if request.method=='POST':
        fname=request.POST.get('fn')
        lname=request.POST.get('ln')
        email=request.POST.get('email')
        contactno=request.POST.get('contact')
        password=request.POST.get('pwd')
        confirmpassword=request.POST.get('cpwd')
        address=request.POST.get('adr')
        print(fname)
        print(lname)
        print(email)
        print(contactno)
        print(password)
        print(confirmpassword)
        print(address)

        us = patient.objects.filter(email = email) 
        k=len(us)

        if k>0:
            res= "1"
            return render(request,'register.html',{'res':res})
        else:
            if (password==confirmpassword):
                pat=patient()
                pat.Name=fname+" "+lname
                pat.email=email
                pat.contact=contactno
                pat.password=password
                pat.address=address
                pat.save()
                return redirect('/login')
            else:
                res="2"
                return render(request,'register.html',{'res':res})

        
    return render(request,'register.html',{})

def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        us= patient.objects.filter(email = email , password = password)  
        k=len(us)
        if k>0:
            print("valid credentials ")
            request.session['email'] = email

            return redirect('/profile')
   
           
        else:

            print("invalid credentials ")
            res="1"
            return render(request,'login.html',{'error':res})

    return render(request,'login.html',{})


def recover(request):
    return render(request,'recover.html',{})
 
 
def contactus(request):
    if request.method == 'POST':
        
        name=request.POST.get('fn')
        email=request.POST.get('email')
        subject=request.POST.get('ln')
        message=request.POST.get('Suggestion')
        print(message)
        print(name)
        print(email)
        print(subject)

        cont=contact()
        cont.name=name
        cont.email=email
        cont.subject=subject
        cont.message=message
        cont.save()

    return render(request,'contactus.html',{})


def aboutus(request):
    return render(request,'aboutus.html',{})


def footer(request):
    return render(request,'footer.html',{})

def forgot(request):
    if (request.method=='POST'):
        em=request.POST.get('email')
        user=patient.objects.filter(email=em)
        
        if (len(user)>0):
            pw=user[0].password
            subject="Password"
            message="Welcome . your Password is " + pw
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em,]
            send_mail(subject,message,email_from,recipient_list)
            rest="your password is sent to your repective email account. Please check"
            return render(request,'forgot.html',{'rest':rest})
        else:
            res="This email id is not registered"
            return render(request,'forgot.html',{'res':res})
    else:
        return render(request,'forgot.html')
      

def allappointment(request):

    if not  request.session.has_key('email'):
        return redirect('/login')
    else:    
        email=request.session.get("email")
        pat_data=patient.objects.get(email=email)
        appointments=appointment_table.objects.filter(patient_id=pat_data)

        selected_field = 'all'
        entered_date = date.today().strftime("%Y-%m-%d")
        print(appointments)

        if request.method == 'POST':

            type_of_form = request.POST.get('type')
            print(type_of_form)
            if type_of_form == "1":
                app_filter = request.POST.get('status')
                filter_date = request.POST.get('date')
                print(app_filter,filter_date)

               
                appointments, selected_field, entered_date = get_user_appointments_from_status(app_filter, filter_date, pat_data)

           
        return render(request,'allappointments.html',{'appointments':appointments, 'selected_field': selected_field, 'entered_date':entered_date})
    
    # if request.method == 'POST':
    #     app_filter = request.POST.get('status')
    #     filter_date = request.POST.get('date')
    #     print(app_filter,filter_date)

    #     if app_filter == 'all':
    #         appointments = appointment_table.objects.filter(apply_date=filter_date, patient_id=pat_data)
    #         print('All appointments',appointments)

    #     if app_filter == 'pending':
    #         appointments = appointment_table.objects.filter(status='P', apply_date=filter_date, patient_id=pat_data)
    #         print('Pending appointments',appointments)

    #     if app_filter == 'cancelled':
    #         appointments = appointment_table.objects.filter(status='NA', apply_date=filter_date, patient_id=pat_data)
    #         print('cancelled appointments',appointments)

    #     if app_filter == 'approved':
    #         appointments = appointment_table.objects.filter(status='A', apply_date=filter_date, patient_id=pat_data)
    #         print('approved appointments',appointments)
    
    # return render(request,'allappointments.html',{'appointments':appointments})  

def get_user_appointments_from_status(app_filter, filter_date, pat_data):

    if app_filter == 'all':
        appointments = appointment_table.objects.filter(Date=filter_date, patient_id=pat_data)
        selected_field = app_filter
        entered_date = filter_date
        print('All appointments',appointments)

    elif app_filter == 'pending':
        appointments = appointment_table.objects.filter(status='P', Date=filter_date, patient_id=pat_data)
        selected_field = app_filter
        entered_date = filter_date
        print('Pending appointments',appointments)

    elif app_filter == 'rejected':
        selected_field = app_filter
        entered_date = filter_date
        appointments = appointment_table.objects.filter(status='NA', Date=filter_date, patient_id=pat_data)
        print('cancelled appointments',appointments)

    elif app_filter == 'approved':
        selected_field = app_filter
        entered_date = filter_date
        appointments = appointment_table.objects.filter(status='A', Date=filter_date,patient_id=pat_data)
        print('approved appointments',appointments)
 
    return (appointments, selected_field, entered_date)

def get_user_chat_from_status(app_filter, doc_data):

    if  app_filter == 'active':
        appointments = appointment_table.objects.filter(status='A', doctor_id=doc_data)
        selected_field = app_filter  
        print('Active',appointments)
 
    elif app_filter == 'not active':
        selected_field = app_filter
        appointments = appointment_table.objects.filter(status='NA', doctor_id=doc_data)
        print('Not Active',appointments)

    
    return (appointments, selected_field)

def get_doc_chat_from_status(app_filter, pat_data):

    if  app_filter == 'active':
        appointments = chat_table.objects.filter(status='A', patient_id=pat_data)
        selected_field = app_filter  
        print('Active',appointments)
 
    elif app_filter == 'not active':
        selected_field = app_filter
        appointments = chat_table.objects.filter(status='NA', patient_id=pat_data)
        print('Not Active',appointments)

    
    return (appointments, selected_field)



def blog(request):
    blogss =  blogs.objects.all()  

    return render(request,'blog.html',{'blogs':blogss}) 

def disease(request):
    disease =  diseases.objects.all()  

    return render(request,'disease.html',{'disease':disease}) 

def nav_doctors(request):
    doctors =  doctor.objects.all()   
    return render(request,'nav_doctors.html',{'doctors': doctors}) 

def nav_hospitals(request):
    hosps=hospital.objects.all()
    print(hosps)

    return render(request,'nav_hospitals.html',{'hosps':hosps})

def nav_labs(request):
    lab=labs.objects.all()
    print(lab)

    return render(request,'nav_labs.html',{'lab':lab})
           



def doctors_view(request):
    if not  request.session.has_key('email'):
        return redirect('/login')

    doctors =  doctor.objects.all()    
    return render(request,'doctors.html',{'doctors': doctors})    

#MVT Model View Template


def changepassword(request):
    if not  request.session.has_key('email'):
        return redirect('/login')

    if request.method=='POST':
        usr=patient.objects.get(email=request.session['email'])
        opw=(request.POST.get('opwd'))
        npw=(request.POST.get('pwd'))
        cnpw=(request.POST.get('cpwd'))
      
        if(npw==cnpw):
            p=usr.password
            if(opw==p):
                usr.password=npw
                usr.save()
                print("password has been changed")
                res="1"
                return render(request, 'changepassword.html', {'res':res})
            else:
                print("doesnt match with confirm password")
                res = "2"
                return render(request,'changepassword.html', {'res':res})
        else:
            res = "3"
            return render(request,'changepassword.html',{'res':res})

    return render(request,'changepassword.html',{})    

def editprofile(request):
    if not  request.session.has_key('email'):
        return redirect('/login')

    if request.method=='POST':

        form_type =  request.POST.get('type')
        print(form_type)
        if form_type == "1":
            image = request.FILES.get('image')

            email=request.session.get("email")
            pat_data=patient.objects.get(email=email) #retrieve data from model of current user

            pat_data.profile_image = image
            pat_data.save()
            return redirect('/editprofile')
       
        else:

            name=request.POST.get('fn')       
            contact=request.POST.get('phn')
            city=request.POST.get('city')
            state=request.POST.get('state')
            gender=request.POST.get('gen')
            dob=request.POST.get('dob')        
            address=request.POST.get('address')

            email=request.session.get("email")
            pat_data=patient.objects.get(email=email)

            pat_data.Name = name
            pat_data.contact=contact
            pat_data.city=city
            pat_data.state=state
            pat_data.gender=gender
            pat_data.dob=dob
            pat_data.address=address

            print( pat_data.dob)

            pat_data.save()



    email=request.session.get("email")
    pat_data=patient.objects.get(email=email)

    if pat_data.dob:
        pat_dob = pat_data.dob.strftime('%Y-%m-%d')
        return render(request,'editprofile.html',{'pat_data':pat_data, 'pat_dob':pat_dob}) 

    return render(request,'editprofile.html',{'pat_data':pat_data}) 
    

def header(request):
    return render(request,'header.html',{})   

def helpsupport(request):
    
    if not  request.session.has_key('email'):
        return redirect('/login')

    if request.method=='POST':
        h = helpandsupport()
        h.subject = request.POST.get('sub')
        h.message = request.POST.get('message')
        h.user_email = request.session.get('email')
        h.save()
        return render(request,'helpsupport.html',{})

    else:

        return render(request,'helpsupport.html',{})   
        
def profile(request):
    if not  request.session.has_key('email'):
        return redirect('/login')

    email=request.session.get("email")
    pat_data=patient.objects.get(email=email)
    return render(request,'profile.html',{'pat_data': pat_data})  

def review(request):
    return render(request,'review.html',{})  

def front(request):
    context={}
    hospitals = hospital.objects.all()[0:6]
    doc = doctor.objects.all()[0:4]
    context={'hosp':hospitals,
    'doc':doc}
    return render(request,'front.html',context)  

def base(request):
    return render(request,'base.html',{})   

def doc_profile(request, doc_id ):

    if not request.session.has_key('email'):
        pass
    doc = doctor.objects.get(id = doc_id)
    return render(request,'doc_profile.html',{'doc':doc}) 

def fullblog(request, id ):

    blogss =  blogs.objects.get(id=id)  
    return render(request,'fullblog.html',{'blogs':blogss}) 

def hospitaldetail(request, id ):

    hospitals = hospital.objects.get(id = id)
    return render(request,'hospitaldetail.html',{'hospitals':hospitals})

def labdetail(request, id ):

    labdetails = labs.objects.get(id = id)
    return render(request,'labdetail.html',{'labdetails':labdetails})    
         

def nav_doc_profile(request, doc_id ):

    doc = doctor.objects.get(id = doc_id)
    return render(request,'nav_doc_profile.html',{'doc':doc}) 

def appointment(request, doc_id):
    if not  request.session.has_key('email'):
        return redirect('/login')
    
    user=patient.objects.get(email = request.session.get('email'))
    res = None
    if request.method == 'POST':
        cur_user = patient.objects.get(email = request.session.get('email'))
        doct = doctor.objects.get(id = doc_id)  
        #get all data
        desc = request.POST.get('des')
        appointment_date = request.POST.get('date')
        appointment_time = request.POST.get('time')

        print(desc, appointment_date, appointment_time)
      
        app = appointment_table()
        app.patient_id = cur_user
        app.doctor_id = doct
        app.Date = appointment_date
        app.Time = appointment_time
        app.apply_date = date.today()
        app.is_active = False
        app.description = desc
        app.save()

        res = 'Appointment Applied'
       

    return render(request,'appointment.html',{'user':user, 'res':res})

def chatbox(request,id=None):
    if not  request.session.has_key('email'):
        return redirect('/login')

    


    if request.method == 'POST':
        msg = request.POST.get('msg')
        attachment = request.FILES.get('attachment')
        app_id  = request.POST.get('app_id')
        doc_email = request.POST.get('doc_email')
        print(doc_email)
        message = Message()

        message.Message = msg
        message.From = request.session.get('email')
        message.to = doc_email
        date_time_today = datetime.today()
        message.Date = date_time_today.date()
        message.Time = date_time_today.time()

        message.appointment_id = appointment_table.objects.get(id = app_id)

        if attachment:
            message.Attachment = attachment

        message.save()



        print(msg, attachment, app_id)

        return JsonResponse({'name':'sourabh'})
    
   
    appointment_detail = appointment_table.objects.get(id = id)
    messages = Message.objects.filter(appointment_id = appointment_detail)

    return render(request,'chatbox.html',{'appointment_detail': appointment_detail, 'messages':messages})     

def chat_table(request):
    if not  request.session.has_key('email'):
        return redirect('/login')
    else:    
        email=request.session.get("email")
        pat_data=patient.objects.get(email=email)

        appointments =appointment_table.objects.filter(patient_id=pat_data, status = 'A', is_active= True)
              
        
        return render(request,'chat_table.html',{'appointments':appointments,})
    
# def doc_chats_table(request):
#     if not  request.session.has_key('doc_email'):
#         return redirect('/login')
#     else:    
#         email=request.session.get("email")
#         doc_data=patient.objects.get(Email=email)
#         chats=chat_table.objects.filter(doctor_id=doc_data)
        
#         selected_field = 'active'
#         print(chats)

#         if request.method == 'POST':

#             type_of_form = request.POST.get('type')
#             print(type_of_form)
#             if type_of_form == "1":
#                 app_filter = request.POST.get('status')
#                 print(app_filter)

               
#                 appointments, selected_field = get_user_chat_from_status(app_filter, doc_data)

           
#         return render(request,'chat_table.html',{'appointments':appointments, 'selected_field': selected_field})
        
def hosp(request):
    if not  request.session.has_key('email'):
        return redirect('/login')

    hosps=hospital.objects.all()
    print(hosps)

    return render(request,'hosp.html',{'hosps':hosps})         


#############################Doctor panel#########################################

def doc_login(request):
    
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        doc= doctor.objects.filter(Email = email , password = password)  
        k=len(doc)
        if k>0:
            print("valid credentials ")
            request.session['doc_email'] = email
            return redirect('/doctor_profile')

            #return redirect('Doctor_panel/doctor_profile.html',{})
   
           
        else:

            print("invalid credentials ")
            res="1"
            return render(request,'Doctor_panel/doc_login.html',{'error':res})

    return render(request,'Doctor_panel/doc_login.html',{})

def doctor_profile(request):

    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')

    email=request.session.get("doc_email")
    doc_data=doctor.objects.get(Email=email)
    print(doc_data,email)
    return render(request,'Doctor_panel/doctor_profile.html',{'doc_data': doc_data})  

def doc_changepassword(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    
    if request.method=='POST':
        doc=doctor.objects.get(Email=request.session['doc_email'])
        opw=(request.POST.get('opwd'))
        npw=(request.POST.get('pwd'))
        cnpw=(request.POST.get('cpwd'))
      
        if(npw==cnpw):
            p=doc.password
            if(opw==p):
                doc.password=npw
                doc.save()
                print("password has been changed")
                res="1"
                return render(request, 'Doctor_panel/doc_changepassword.html', {'res':res})
            else:
                print("doesnt match with confirm password")
                res = "2"
                return render(request,'Doctor_panel/doc_changepassword.html', {'res':res})
        else:
            res = "3"
            return render(request,'Doctor_panel/doc_changepassword.html',{'res':res})

    return render(request,'Doctor_panel/doc_changepassword.html',{}) 
     
def doc_chat_table(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
 
    email=request.session.get("doc_email")
    doc_data=doctor.objects.get(Email=email)
    selected_field = 'active'
    # print(doc_data)
    # print(email)


    if request.method == 'POST':
        status = request.POST.get('status')
        if status == 'active':
            appointments=appointment_table.objects.filter(doctor_id=doc_data, status='A', is_active=True)

        elif status == 'not_active':
            appointments=appointment_table.objects.filter(doctor_id=doc_data, status='A', is_active=False)
                
        selected_field = status
        print(status)

    else:
        appointments=appointment_table.objects.filter(doctor_id=doc_data, status='A', is_active=True)

   

    print(appointments)
    return render(request,'Doctor_panel/doc_chat_table.html',{'appointment':appointments, 'selected_field':selected_field})     

def doc_chat_box(request,id):
    return render(request, 'Doctor_panel/doc_chatbox.html' , {})
def doc_editprofile(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')

    if request.method=='POST':

        form_type =  request.POST.get('type')
        print(form_type)
        if form_type == "1":
            image = request.FILES.get('image')

            email=request.session.get("doc_email")
            doc_data=doctor.objects.get(Email=email) #retrieve data from model of current user

            doc_data.profile_image = image
            
            doc_data.save()
            
            
       
        else:

            name=request.POST.get('fn')       
            contact=request.POST.get('phn')
            city=request.POST.get('city')
            state=request.POST.get('state')
            gender=request.POST.get('gen')
            dob=request.POST.get('dob')        
            address=request.POST.get('address')

            email=request.session.get("doc_email")
            doc_data=doctor.objects.get(Email=email)

            doc_data.name = name
            doc_data.contact=contact
            doc_data.city=city
            doc_data.state=state
            doc_data.gender=gender
            #doc_data.dob=dob
            doc_data.address=address

            doc_data.save()

           


 
    email=request.session.get("doc_email")
    doc_data=doctor.objects.get(Email=email)

    if doc_data.dob:
        doc_dob = doc_data.dob.strftime('%Y-%m-%d')
        return render(request,'Doctor_panel/doc_editprofile.html',{'doc_data':doc_data, 'doc_dob':doc_dob}) 
    
    return render(request,'Doctor_panel/doc_editprofile.html',{'doc_data':doc_data}) 
    

    # return render(request,'Doctor_panel/doc_editprofile.html',{})    
# def review(request):
#     return render(request,'Doctor_panel/profile.html',{})  

def get_appointments_from_status(app_filter, filter_date, doc_data):

    if app_filter == 'all':
        appointments = appointment_table.objects.filter(Date=filter_date, doctor_id=doc_data)
        selected_field = app_filter
        entered_date = filter_date
        print('All appointments',appointments)

    elif app_filter == 'pending':
        appointments = appointment_table.objects.filter(status='P', Date=filter_date, doctor_id=doc_data)
        selected_field = app_filter
        entered_date = filter_date
        print('Pending appointments',appointments)

    elif app_filter == 'rejected':
        selected_field = app_filter
        entered_date = filter_date
        appointments = appointment_table.objects.filter(status='NA', Date=filter_date, doctor_id=doc_data)
        print('cancelled appointments',appointments)

    elif app_filter == 'approved':
        selected_field = app_filter
        entered_date = filter_date
        appointments = appointment_table.objects.filter(status='A', Date=filter_date, doctor_id=doc_data)
        print('approved appointments',appointments)
 
    return (appointments, selected_field, entered_date)

def patient_appointment(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    else:   
        email=request.session.get("doc_email")
        doc_data=doctor.objects.get(Email=email)
        print(doc_data)
        print(email)
        appointments=appointment_table.objects.filter(doctor_id=doc_data, Date=date.today())
        selected_field = 'all'
        entered_date = date.today().strftime("%Y-%m-%d")
        print(appointments)

        if request.method == 'POST':

            type_of_form = request.POST.get('type')
            print(type_of_form)
            if type_of_form == "1":
                app_filter = request.POST.get('status')
                filter_date = request.POST.get('date')
                print(app_filter,filter_date)

                appointments, selected_field, entered_date = get_appointments_from_status(app_filter, filter_date, doc_data)

                      
            elif type_of_form == "2":
                appointment_id = request.POST.get('app_id')
                reason = request.POST.get('reason')
                appointment = appointment_table.objects.get(id = appointment_id)
                appointment.status = 'NA'
                appointment.description = reason
                appointment.is_active = False
                appointment.save()
                app_filter= request.POST.get('app_filter')
                filter_date = request.POST.get('date')

                appointments, selected_field, entered_date = get_appointments_from_status(app_filter, filter_date, doc_data)


            elif type_of_form == "3":
                appointment_id = request.POST.get('app_id')
                appointment = appointment_table.objects.get(id = appointment_id)
                appointment.status = 'A'
                appointment.is_active = True
                appointment.save()
                app_filter= request.POST.get('app_filter')
                filter_date = request.POST.get('date')
                
                appointments, selected_field, entered_date = get_appointments_from_status(app_filter, filter_date, doc_data)

           
        return render(request,'Doctor_panel/patient_appointment.html',{'appointments':appointments, 'selected_field': selected_field, 'entered_date':entered_date})
def doc_forgot(request):
    if (request.method=='POST'):
        em=request.POST.get('doc_email')
        user=doctor.objects.filter(Email=em)
        
        if (len(user)>0):
            pw=user[0].password
            subject="Password"
            message="Welcome . your Password is " + pw
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em,]
            send_mail(subject,message,email_from,recipient_list)
            rest="your password is sent to your repective email account. Please check"
            return render(request,'Doctor_panel/forgot.html',{'rest':rest})
        else:
            res="This email id is not registered"
            return render(request,'Doctor_panel/doc_forgot.html',{'res':res})
    else:
        return render(request,'Doctor_panel/doc_forgot.html')


def tumor_detection(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    if request.method=='POST':
        f = request.FILES['image'] # here you get the files needed
        handle_uploaded_file(f,'static/predict.jpg')
        from tensorflow.keras.models import load_model

        classifier = load_model('brain_tumor_dataset_model.h5')
        import numpy as np
        from keras.preprocessing import image
        test_image =image.load_img(f.name,target_size =(64,64))
        test_image =image.img_to_array(test_image)
        test_image =np.expand_dims(test_image, axis =0)
        result = classifier.predict(test_image)
        print(result)
        
        prediction=''
        if result[0][0] >= 0.5:
            prediction = 'Yes, it might be a Tumor'
            return render(request,'Doctor_panel/yes_tumor_detection.html',{'p':prediction,'name':'static/'+f.name})

        else:
            prediction = 'No Tumor'
            return render(request,'Doctor_panel/no_tumor_detection.html',{'p':prediction,'name':'static/'+f.name})

        print(prediction)

    else:    
        return render(request,'Doctor_panel/tumor_detection.html',{})

def yes_tumor_detection(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    
    return render(request,'Doctor_panel/yes_tumor_detection.html',{})


def no_tumor_detection(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    
    return render(request,'Doctor_panel/no_tumor_detection.html',{})

def advance_tumor_detection(request):

    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')

    if request.method=='POST':
        f= request.FILES['image']
        handle_uploaded_file(f,'static/predict.jpg')
        from tensorflow.keras.models import load_model
        
        classifier = load_model('brain_cnn_modelnew.h5')
        import numpy as np
        from keras.preprocessing import image
        test_image =image.load_img(f.name,target_size =(64,64))
        test_image =image.img_to_array(test_image)
        test_image =np.expand_dims(test_image, axis =0)
        result = classifier.predict(test_image)
        print(result)    
        prediction=''
        if result[0][0]>= 0.5:
            prediction = 'Glioma Tumor'
            return render(request,'Doctor_panel/glioma_tumor.html',{'p':prediction,'name':'static/'+f.name})

        elif result[0][1] >= 0.5:
            prediction = 'Meningioma Tumor'
            return render(request,'Doctor_panel/mening_tumor.html',{'p':prediction,'name':'static/'+f.name})
        elif result[0][2] >= 0.5:
            prediction = 'No Tumor'
            return render(request,'Doctor_panel/no_tumor.html',{'p':prediction,'name':'static/'+f.name})
        else:
            prediction = 'Pituitary Tumor'
            return render(request,'Doctor_panel/pituitary_tumor.html',{'p':prediction,'name':'static/'+f.name})
          
       
    else:
        return render(request,'Doctor_panel/advance_tumor_detection.html',{})

def advance_tumor_results(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    return render(request,'Doctor_panel/advance_tumor_detection.html',{})  

def glioma_tumor(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    
    return render(request,'Doctor_panel/glioma_tumor.html',{})

def pituitary_tumor(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    
    return render(request,'Doctor_panel/pituitary_tumor.html',{})

def mening_tumor(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    
    return render(request,'Doctor_panel/mening_tumor.html',{})

def no_tumor(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    
    return render(request,'Doctor_panel/no_tumor.html',{})    

def handle_uploaded_file(f,name):
    destination = open(name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


def doc_logout(request):
    if not request.session.has_key('doc_email'):
        return redirect('/doc_login')
    else:
        del request.session['doc_email']
        return redirect('/doc_login')
    

def upload_file(f,name):

    destination = open("media/"+name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    
    destination.close()






# def temp_Appointment(request):
#     doc = mydoctor.objects.get(doc_email = request.session['docem'])

#     if request.method == 'POST':
#             app_filter = request.POST.get('filter')
#             filter_date = request.POST.get('date')
#             print(app_filter,filter_date)

#             if app_filter == 'pending_appointments':
#                 appointments = myappointment.objects.filter(app_status='P', app_date = filter_date, doctor_id = doc)
#                 return render(request,'doctorF/docappointment.html',{'appointments':appointments, 'selected_field': app_filter, 'entered_date': filter_date})

#             elif app_filter == 'approved_appointments':
#                 appointments = myappointment.objects.filter(app_status='A', app_date = filter_date,doctor_id = doc)
#                 return render(request,'doctorF/docappointment.html',{'appointments':appointments, 'selected_field': app_filter, 'entered_date': filter_date})
#             elif app_filter == 'all_appointments':
#                 appointments = myappointment.objects.filter(app_date = filter_date,doctor_id = doc)
#                 return render(request,'doctorF/docappointment.html',{'appointments':appointments, 'selected_field': app_filter, 'entered_date': filter_date})    

#             elif app_filter == 'rejected_appointments':
#                 appointments = myappointment.objects.filter(app_status='NA', app_date = filter_date,doctor_id = doc)
#                 return render(request,'doctorF/docappointment.html',{'appointments':appointments, 'selected_field': app_filter, 'entered_date': filter_date})    

  
#     # will show all apointments of today
#     appointments = myappointment.objects.filter(doctor_id = doc, app_date = date.today())
#     return render(request,'doctorF/docappointment.html',{'appointments':appointments, 'entered_date': date.today().strftime('%Y-%m-%d')} )
