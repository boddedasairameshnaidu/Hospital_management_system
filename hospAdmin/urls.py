"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.hms,name='hms'),
    path('admpage/',views.admpage,name='admpage'),
    path('adminloginaction/',views.adminloginaction,name='adminloginaction'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('patientpage/',views.patientpage,name='patientpage'),
    path('addpatient/',views.addpatient,name='addpatient'),
    path('addpatientaction/',views.addpatientaction,name='addpatientaction'),
    path('updatepatient/',views.updatepatient,name='updatepatient'),
    path('searchpatientaction/',views.searchpatientaction,name='searchpatientaction'),
    path('updatepatientaction/',views.updatepatientaction,name='updatepatientaction'),
    path('deletepatient/',views.deletepatient,name='deletepatient'),
    path('deletepatientaction/',views.deletepatientaction,name='deletepatientaction'),
    path('searchpatient/',views.searchpatient,name='searchpatient'),
    path('searchpatientactionmain/',views.searchpatientactionmain,name='searchpatientactionmain'),
    path('viewpatient/',views.viewpatient,name='viewpatient'),
    path('doctorpage/',views.doctorpage,name='doctorpage'),
    path('adddoctor/',views.adddoctor,name='adddoctor'),
    path('adddoctoraction/',views.adddoctoraction,name='adddoctoraction'),
    path('updatedoctor/',views.updatedoctor,name='updatedoctor'),
    path('searchdoctoraction/',views.searchdoctoraction,name='searchdoctoraction'),
    path('updatedoctoraction/',views.updatedoctoraction,name='updatedoctoraction'),
    path('deletedoctor/',views.deletedoctor,name='deletedoctor'),
    path('deletedoctoraction/',views.deletedoctoraction,name='deletedoctoraction'),
    path('searchdoctor/',views.searchdoctor,name='searchdoctor'),
    path('searchdoctoractionmain/',views.searchdoctoractionmain,name='searchdoctoractionmain'),
    path('viewdoctor/',views.viewdoctor,name='viewdoctor'),
    path('receptionistpage/',views.receptionistpage,name='receptionistpage'),
    path('addreceptionist/',views.addreceptionist,name='addreceptionist'),
    path('addreceptionistaction/',views.addreceptionistaction,name='addreceptionistaction'),
    path('updatereceptionist/',views.updatereceptionist,name='updatereceptionist'),
    path('searchreceptionistaction/',views.searchreceptionistaction,name='searchreceptionistaction'),
    path('updatereceptionistaction/',views.updatereceptionistaction,name='updatereceptionistaction'),
    path('deletereceptionist/',views.deletereceptionist,name='deletereceptionist'),
    path('deletereceptionistaction/',views.deletereceptionistaction,name='deletereceptionistaction'),
    path('searchreceptionist/',views.searchreceptionist,name='searchreceptionist'),
    path('searchreceptionistactionmain/',views.searchreceptionistactionmain,name='searchreceptionistactionmain'),
    path('viewreceptionist/',views.viewreceptionist,name='viewreceptionist'),
    path('doclogin/',views.doclogin,name='doclogin'),
    path('docloginaction/',views.docloginaction,name='docloginaction'),
    path('docviewappointments/',views.docviewappointments,name='docviewappointments'),
    path('receplogin/',views.receplogin,name='receplogin'),
    path('receploginaction/',views.receploginaction,name='receploginaction'),
    path('bookappointment/',views.bookappointment,name='bookappointment'),
    path('searchdocbydept/',views.searchdocbydept,name='searchdocbydept'),
    path('selectdoctoraction/',views.selectdoctoraction,name='selectdoctoraction'),
    path('selectpatientbyId/',views.selectpatientbyId,name='selectpatientbyId'),
    path('makeappointment/',views.makeappointment,name='makeappointment'),
    path('delapprecord/',views.delapprecord,name='delapprecord'),
    path('goback/',views.goback,name='goback'),
    path('gobackpatient/',views.gobackpatient,name='gobackpatient'),
    path('gobackdoc/',views.gobackdoc,name='gobackdoc'),
    path('gobackrecep/',views.gobackrecep,name='gobackrecep'),
    path('gobackdoctor/',views.gobackdoctor,name='gobackdoctor'),
    path('doclogout/',views.doclogout,name='doclogout'),
    path('receplogout/',views.receplogout,name='receplogout'),
    path('gobackrecep/',views.gobackrecep,name='gobackrecep'),
    path('addpatientrecep/',views.addpatientrecep,name='addpatientrecep'),
    path('addpatientrecepaction/',views.addpatientrecepaction,name='addpatientrecepaction'),
    path('searchpatientrecep/',views.searchpatientrecep,name='searchpatientrecep'),
    path('updatepatientrecepaction/',views.updatepatientrecepaction,name='updatepatientrecepaction'),
    path('updatepatientrecep/',views.updatepatientrecep,name='updatepatientrecep'),
    path('deletepatientrecep/',views.deletepatientrecep,name='deletepatientrecep'),
    path('deletepatientrecepaction/',views.deletepatientrecepaction,name='deletepatientrecepaction'),
    path('searchpatientrecep/',views.searchpatientrecep,name='searchpatientrecep'),
    path('searchpatientrecepactionmain/',views.searchpatientrecepactionmain,name='searchpatientrecepactionmain'),
]
