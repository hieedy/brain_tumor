"""braintumor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',views.form,name='form'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('recover/',views.recover,name='recover'),
    path('contactus/',views.contactus,name='contactus'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('footer/',views.footer,name='footer'),
    path('forgot/',views.forgot,name='forgot'),
    path('doc_forgot/',views.doc_forgot,name='doc_forgot'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('header/',views.header,name='header'),
    path('helpsupport/',views.helpsupport,name='helpsupport'),
    path('profile/',views.profile,name='profile'),
    path('review/',views.review,name='review'),
    path('front/',views.front,name='front'),
    path('blog/',views.blog,name='blog'),
    path('disease/',views.disease,name='disease'),
    path('doctors/',views.doctors_view,name='doctors'),
    path('doc_profile/<int:doc_id>',views.doc_profile,name='doc_profile'),
    path('nav_doc_profile/<int:doc_id>',views.nav_doc_profile,name='nav_doc_profile'),
    path('appointment/<int:doc_id>',views.appointment,name='appointment'),
    path('hospitaldetail/<int:id>',views.hospitaldetail,name='hospitaldetail'),
    path('fullblog/<int:id>',views.fullblog,name='fullblog'),
    path('labdetail/<int:id>',views.labdetail,name='labdetail'),
    path('chatbox/',views.chatbox,name='chatbox'),
    path('chatbox/<int:id>',views.chatbox,name='chatbox'),
    path('base/',views.base,),
    path('logout/', views.logout, name='logout'),
    path('allappointments/', views.allappointment, name='allappointments'),
    path('hospital', views.hosp, name='hospital'),
    path('chat_table/', views.chat_table, name='chat_table'),
    path('doc_chat_box/<int:id>', views.doc_chat_box, name='doc_chat_box'),

    path('doc_chat_table/', views.doc_chat_table, name='doc_chat_table'),
    path('nav_doctors/', views.nav_doctors, name='nav_doctors'),
    path('nav_hospitals/', views.nav_hospitals, name='nav_hospitals'),
    path('nav_labs/', views.nav_labs, name='nav_labs'),
    #####################Doctor panel
    path('doc_changepassword/', views.doc_changepassword, name='doc_changepassword'),
    path('doc_login/',views.doc_login,name='doc_login'),
    path('doctor_profile/',views.doctor_profile,name='doctor_profile'),
    path('doc_editprofile/',views.doc_editprofile,name='doc_editprofile'),
    path('patient_appointment/',views.patient_appointment,name='patient_appointment'),
    path('tumor_detection/',views.tumor_detection,name='tumor_detection'),
    path('no_tumor_detection/',views.no_tumor_detection,name='no_tumor_detection'),
    path('yes_tumor_detection/',views.yes_tumor_detection,name='yes_tumor_detection'),
    path('advance_tumor_detection/',views.advance_tumor_detection,name='advance_tumor_detection'),
    path('advance_tumor_results/',views.advance_tumor_results,name='advance_tumor_results'),
    path('glioma_tumor/',views.glioma_tumor,name='glioma_tumor'),
    path('pituitary_tumor/',views.pituitary_tumor,name='pituitary_tumor'),
    path('no_tumor/',views.no_tumor,name='no_tumor'),
    path('mening_tumor/',views.mening_tumor,name='mening_tumor'),
    path('doc_logout/',views.doc_logout,name='doc_logout'),
    
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
