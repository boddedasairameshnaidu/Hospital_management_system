from django.shortcuts import render
from .models import *
from datetime import datetime
# Create your views here.
def hms(request):
    return render(request,'admhome.html')

def admpage(request):
    return render(request,'adminlogin.html')

def adminloginaction(request):
    try:
        if request.method == 'POST' and request.POST['name'] == 'admin' and request.POST['pwd'] == 'admin':
            return render(request,'admpage.html')
        else:
            raise Exception
    except:
        stz = True
        msg = 'Invalid Credentials'
        return render(request,'adminlogin.html',{'msg':msg,'stz':stz})
    
def adminlogout(request):
    return render(request,'admhome.html')

def patientpage(request):
    return render(request,'patientpage.html')

def addpatient(request):
    return render(request,'addpatient.html')

def addpatientrecep(request):
    return render(request,'addpatientrecep.html')

def addpatientaction(request):
        if request.method == 'POST':
            date = request.POST['date']
            address = request.POST['address']
            id = request.POST['id']
            phone = request.POST['phone']
            name = request.POST['name']
            marital_status = request.POST['marital_status']
            age = request.POST['age']
            gender = request.POST['gender']
            disease = request.POST['disease']
            blood_group = request.POST['blood_group']
            d = Patientinfo.objects.filter(phone=phone).count()
            if d == 0:
                d = Patientinfo(date=date,address=address,id=id,phone=phone,name=name,marital_status=marital_status,age=age,gender=gender,disease=disease,blood_group=blood_group)
                d.save()
                return render(request,'patientpage.html')
            else:
                msg = 'Patient already exist...'
                stz = True
                return render(request,'addpatient.html',{'msg':msg,'stz':stz})

def addpatientrecepaction(request):
        if request.method == 'POST':
            date = request.POST['date']
            address = request.POST['address']
            id = request.POST['id']
            phone = request.POST['phone']
            name = request.POST['name']
            marital_status = request.POST['marital_status']
            age = request.POST['age']
            gender = request.POST['gender']
            disease = request.POST['disease']
            blood_group = request.POST['blood_group']
            d = Patientinfo.objects.filter(phone=phone).count()
            if d == 0:
                d = Patientinfo(date=date,address=address,id=id,phone=phone,name=name,marital_status=marital_status,age=age,gender=gender,disease=disease,blood_group=blood_group)
                d.save()
                return render(request,'receppage.html')
            else:
                msg = 'Patient already exist...'
                stz = True
                return render(request,'addpatientrecep.html',{'msg':msg,'stz':stz})
    
def updatepatient(request):
    return render(request,'updatepatient.html')

def searchpatientrecep(request):
    if request.method == 'GET':
        id = request.GET['search_query']  
        d = Patientinfo.objects.filter(id=id).all()
        return render(request,'updatepatientrecep.html',{'d':d})
    
def searchpatientaction(request):
    if request.method == 'GET':
        id = request.GET['search_query']  
        d = Patientinfo.objects.filter(id=id).all()
        return render(request,'updatepatient.html',{'d':d})

def updatepatientaction(request):
    if request.method == 'POST':
        date = request.POST['date']
        address = request.POST['address']
        id = request.POST['id']
        phone = request.POST['phone']
        name = request.POST['name']
        marital_status = request.POST['marital_status']
        age = request.POST['age']
        gender = request.POST['gender']
        disease = request.POST['disease']
        blood_group = request.POST['blood_group']
        d = Patientinfo.objects.filter(id=id)
        d.delete()
        d = Patientinfo(date=date,address=address,id=id,phone=phone,name=name,marital_status=marital_status,age=age,gender=gender,disease=disease,blood_group=blood_group)
        d.save()
        msg = 'Patient details updated successfully..'
        stz = True
        return render(request,'updatepatient.html',{'msg':msg,'stz':stz})
    
def updatepatientrecep(request):
    return render(request,'updatepatientrecep.html')

def updatepatientrecepaction(request):
    if request.method == 'POST':
        date = request.POST['date']
        address = request.POST['address']
        id = request.POST['id']
        phone = request.POST['phone']
        name = request.POST['name']
        marital_status = request.POST['marital_status']
        age = request.POST['age']
        gender = request.POST['gender']
        disease = request.POST['disease']
        blood_group = request.POST['blood_group']
        d = Patientinfo.objects.filter(id=id)
        d.delete()
        d = Patientinfo(date=date,address=address,id=id,phone=phone,name=name,marital_status=marital_status,age=age,gender=gender,disease=disease,blood_group=blood_group)
        d.save()
        msg = 'Patient details updated successfully..'
        stz = True
        return render(request,'updatepatientrecep.html',{'msg':msg,'stz':stz})

def deletepatient(request):
    return render(request,'deletepatient.html')

def deletepatientrecep(request):
    return render(request,'deletepatientrecep.html')

def deletepatientaction(request):
    if request.method == 'GET':
        id = request.GET['delete_query']
        d = Patientinfo.objects.filter(id=id).all()
        d.delete()
        msg = 'Patient details deleted successfully..'
        stz = True
        return render(request,'deletepatient.html',{'msg':msg,'stz':stz})

def deletepatientrecepaction(request):
    if request.method == 'GET':
        id = request.GET['delete_query']
        d = Patientinfo.objects.filter(id=id).all()
        d.delete()
        msg = 'Patient details deleted successfully..'
        stz = True
        return render(request,'deletepatientrecep.html',{'msg':msg,'stz':stz})

def searchpatient(request):
    return render(request,'searchpatient.html')

def searchpatientrecep(request):
    return render(request,'searchpatientrecep.html')

def searchpatientactionmain(request):
    if request.method == 'GET':
        id = request.GET['search_query']  
        d = Patientinfo.objects.filter(id=id).all()
        return render(request,'searchpatient.html',{'d':d})
    
def searchpatientrecepactionmain(request):
    if request.method == 'GET':
        id = request.GET['search_query']  
        d = Patientinfo.objects.filter(id=id).all()
        return render(request,'searchpatientrecep.html',{'d':d})

def viewpatient(request):
    d = Patientinfo.objects.filter().all()
    return render(request,'viewpatient.html',{'d':d})

def doctorpage(request):
    return render(request,'doctorpage.html')

def adddoctor(request):
    return render(request,'adddoctor.html')

def adddoctoraction(request):
    if request.method == 'POST':
        joining_date = request.POST['joining_date']
        dept = request.POST['dept']
        id = request.POST['id']
        phone = request.POST['phone']
        name = request.POST['name']
        email = request.POST['email']
        user_name = request.POST['user_name']
        age = request.POST['age']
        marital_status = request.POST['marital_status']
        pwd = request.POST['pwd']
        gender = request.POST['gender']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        d = DoctorInfo.objects.filter(phone=phone).count()
        if d == 0:
            d = DoctorInfo(joining_date=joining_date,dept=dept,id=id,phone=phone,name=name,email=email,user_name=user_name,age=age,marital_status=marital_status,pwd=pwd,gender=gender,address=address,blood_group=blood_group)          
            d.save()
            return render(request,'doctorpage.html')
        else:
            msg = 'Doctor already exist...'
            stz = True
            return render(request,'adddoctor.html',{'msg':msg,'stz':stz})
        
def updatedoctor(request):
    return render(request,'updatedoctor.html')

def searchdoctoraction(request):
    if request.method == 'GET':
        id = request.GET['search_query']  
        d = DoctorInfo.objects.filter(id=id).all()
        return render(request,'updatedoctor.html',{'d':d})

def updatedoctoraction(request):
    if request.method == 'POST':
        joining_date = request.POST['joining_date']
        dept = request.POST['dept']
        id = request.POST['id']
        phone = request.POST['phone']
        name = request.POST['name']
        email = request.POST['email']
        user_name = request.POST['user_name']
        age = request.POST['age']
        marital_status = request.POST['marital_status']
        pwd = request.POST['pwd']
        gender = request.POST['gender']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        d = DoctorInfo.objects.filter(phone=phone)
        d.delete()
        d = DoctorInfo(joining_date=joining_date,dept=dept,id=id,phone=phone,name=name,email=email,user_name=user_name,age=age,marital_status=marital_status,pwd=pwd,gender=gender,address=address,blood_group=blood_group)          
        d.save()
        msg = 'Doctor details updated successfully..'
        stz = True
        return render(request,'updatedoctor.html',{'msg':msg,'stz':stz})
    
def deletedoctor(request):
    return render(request,'deletedoctor.html')

def deletedoctoraction(request):
    if request.method == 'GET':
        id = request.GET['delete_query']
        d = DoctorInfo.objects.filter(id=id).all()
        d.delete()
        msg = 'Doctor details deleted successfully..'
        stz = True
        return render(request,'deletedoctor.html',{'msg':msg,'stz':stz})

def searchdoctor(request):
    return render(request,'searchdoctor.html')

def searchdoctoractionmain(request):
    if request.method == 'GET':
        id = request.GET['search_query']
        d = DoctorInfo.objects.filter(id=id).all()
        return render(request,'searchdoctor.html',{'d':d})

def viewdoctor(request):
    d = DoctorInfo.objects.filter().all()
    return render(request,'viewdoctor.html',{'d':d})

def receptionistpage(request):
    return render(request,'receptionistpage.html')

def addreceptionist(request):
    return render(request,'addreceptionist.html')

def addreceptionistaction(request):
    if request.method == 'POST':
        joining_date = request.POST['joining_date']
        id = request.POST['id']
        phone = request.POST['phone']
        name = request.POST['name']
        email = request.POST['email']
        user_name = request.POST['user_name']
        age = request.POST['age']
        marital_status = request.POST['marital_status']
        pwd = request.POST['pwd']
        gender = request.POST['gender']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        d = ReceptionistInfo.objects.filter(phone=phone).count()
        if d == 0:
            d = ReceptionistInfo(joining_date=joining_date,id=id,phone=phone,name=name,email=email,user_name=user_name,age=age,marital_status=marital_status,pwd=pwd,gender=gender,address=address,blood_group=blood_group)          
            d.save()
            return render(request,'receptionistpage.html')
        else:
            msg = 'Receptionist already exist...'
            stz = True
            return render(request,'addreceptionist.html',{'msg':msg,'stz':stz}) 

def updatereceptionist(request):
    return render(request,'updatereceptionist.html')

def searchreceptionistaction(request):
    if request.method == 'GET':
        id = request.GET['search_query']  
        d = ReceptionistInfo.objects.filter(id=id).all()
        return render(request,'updatereceptionist.html',{'d':d})

def updatereceptionistaction(request):
    if request.method == 'POST':
        joining_date = request.POST['joining_date']
        id = request.POST['id']
        phone = request.POST['phone']
        name = request.POST['name']
        email = request.POST['email']
        user_name = request.POST['user_name']
        age = request.POST['age']
        marital_status = request.POST['marital_status']
        pwd = request.POST['pwd']
        gender = request.POST['gender']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        d = ReceptionistInfo.objects.filter(phone=phone)
        d.delete()
        d = ReceptionistInfo(joining_date=joining_date,id=id,phone=phone,name=name,email=email,user_name=user_name,age=age,marital_status=marital_status,pwd=pwd,gender=gender,address=address,blood_group=blood_group)          
        d.save()
        msg = 'Receptionist details updated successfully..'
        stz = True
        return render(request,'updatereceptionist.html',{'msg':msg,'stz':stz})

def deletereceptionist(request):
    return render(request,'deletereceptionist.html')

def deletereceptionistaction(request):
    if request.method == 'GET':
        id = request.GET['delete_query']
        d = ReceptionistInfo.objects.filter(id=id).all()
        d.delete()
        msg = 'Receptionist details deleted successfully..'
        stz = True
        return render(request,'deletereceptionist.html',{'msg':msg,'stz':stz})

def searchreceptionist(request):
    return render(request,'searchreceptionist.html')

def searchreceptionistactionmain(request):
    if request.method == 'GET':
        id = request.GET['search_query']
        d = ReceptionistInfo.objects.filter(id=id).all()
        return render(request,'searchreceptionist.html',{'d':d})
    
def viewreceptionist(request):
    d = ReceptionistInfo.objects.filter().all()
    return render(request,'viewreceptionist.html',{'d':d})

def doclogin(request):
    return render(request,'doclogin.html')

def docloginaction(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        pwd = request.POST['pwd']
        d = DoctorInfo.objects.filter(user_name=user_name).filter(pwd=pwd).count()
        if d>0:
            data = DoctorInfo.objects.filter(user_name=user_name).filter(pwd=pwd).first()
            myId = data.id
            request.session['myId'] = myId
            print(myId)
            return render(request,'docpage.html')
        else:
            msg = 'Invalid credentials'
            stz = True
            return render(request,'doclogin.html',{'msg':msg,'stz':stz})
        
def doclogout(request):
    if 'myId' in request.session:
        del request.session['myId']
        return render(request,'admhome.html')
    else:
        msg = 'You are not logged in'
        stz = True
        return render(request,'doclogin.html',{'msg':msg,'stz':stz})

def docviewappointments(request):
    if 'myId' in request.session:
        myId = request.session['myId']
        d = AppointmentsInfo.objects.filter(doc_id=myId).count()
        if d>=1:
            d = AppointmentsInfo.objects.filter(doc_id=myId).all()
            return render(request,'docviewappointments.html',{'d':d})
        else:
            msg = 'No appointments found'
            stz = True
            return render(request,'docviewappointments.html',{'msg':msg,'stz':stz})
    else:
        msg = 'Please login first'
        stz = True
        return render(request,'doclogin.html',{'msg':msg,'stz':stz})

def receplogin(request):
    return render(request,'receplogin.html')


def receploginaction(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        pwd = request.POST['pwd']
        d = ReceptionistInfo.objects.filter(user_name=user_name).filter(pwd=pwd).count()
        if d>0:
            data = ReceptionistInfo.objects.filter(user_name=user_name).filter(pwd=pwd).first()
            recepId = data.id
            request.session['recepId'] = recepId
            return render(request,'receppage.html')
        else:
            msg = 'Invalid credentials'
            stz = True
            return render(request,'receplogin.html',{'msg':msg,'stz':stz})

def receplogout(request):
    if 'recepId' in request.session:
        del request.session['recepId']
        return render(request,'admhome.html')
    else:
        msg = 'You are not logged in'
        stz = True
        return render(request,'receplogin.html',{'msg':msg,'stz':stz})

def bookappointment(request):
    return render(request,'bookappointment.html')

def searchdocbydept(request):
    if request.method == 'GET':
        dept = request.GET['dept']
        d = DoctorInfo.objects.filter(dept=dept).count()
        if d>0:
            d = DoctorInfo.objects.filter(dept=dept).all()
            return render(request,'bookappointment.html',{'d':d})
        else:
            msg = 'No doctors found'
            return render(request,'bookappointment.html',{'msg':msg})
        
def selectdoctoraction(request):
    if request.method == 'POST':
        id = request.POST['id']
        request.session['doc_id'] = id
    x = True
    return render(request,'bookappointment.html',{'x':x})

def selectpatientbyId(request):
    if request.method == 'GET':
        id = request.GET['search_query']
        cnt = Patientinfo.objects.filter(id=id).count()
        if cnt>0:
            data = Patientinfo.objects.filter(id=id).all()
            return render(request,'bookappointment.html',{'data':data})
        else:
            msg = 'No patient found'
            return render(request,'bookappointment.html',{'msg':msg})
 
def makeappointment(request):
    if request.method == 'POST':
        if 'doc_id' in request.session:
            doc_id = request.session['doc_id']
            print(doc_id)
        id = request.POST['id']
        name = request.POST['name']
        disease = request.POST['disease']
        date = request.POST['date']
        d = AppointmentsInfo.objects.filter(patient_id=id,date=date,doc_id=doc_id).count()
        if d==1:
            msg = 'Appointment already exists on this date'
            return render(request,'bookappointment.html',{'msg':msg})
        elif d==0:
            d = AppointmentsInfo(doc_id=doc_id,patient_id=id,patient_name=name,disease=disease,date=date)
            d.save()
            msg = 'Appointment made successfully'
            return render(request,'bookappointment.html',{'msg':msg})
        
def delapprecord(request):
    if request.method == 'POST':
        id = request.POST['id']
        date = request.POST['date']
        # Parse the date string to a datetime object
        date_object = datetime.strptime(date, "%B %d, %Y")
        # Convert the datetime object to the desired format
        formatted_date = date_object.strftime("%Y-%m-%d")
        d = AppointmentsInfo.objects.filter(patient_id=id).filter(date=formatted_date).delete()
        if 'myId' in request.session:
            myId = request.session['myId']
            d = AppointmentsInfo.objects.filter(doc_id=myId).count()
            if d>0:
                d = AppointmentsInfo.objects.filter(doc_id=myId).all()
                return render(request,'docviewappointments.html',{'d':d})
            else:
                msg = 'No appointments found'
                stz = True
                return render(request,'docviewappointments.html',{'msg':msg,'stz':stz})

def goback(request):
    return render(request,'admpage.html')

def gobackpatient(request):
    return render(request,'patientpage.html')

def gobackdoc(request):
    return render(request,'doctorpage.html')

def gobackrecep(request):
    return render(request,'receptionistpage.html')

def gobackdoctor(request):
    return render(request,'docpage.html')

def gobackrecep(request):
    return render(request,'receptionistpage.html')
           