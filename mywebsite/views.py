from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from. models import profile,doctor_profile,patient_profile,appointment


# Create your views here.

def index(request):
    return render(request,"index.html")


def log_in(request):
    return render(request,"login.html")

def  login_check(request):
    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        print(request.POST)
        US = authenticate(username=request.POST['email'], password=request.POST['password'])
        print(US)
        if US is not None:
            login(request,US)
            # return HttpResponse("success")

        else:
            return HttpResponse("Login Failed")

        if request.user.is_superuser:
            return redirect('admin_dashboard')
           # head = profile.objects.filter()
           # info=doctor_profile.objects.all()
           # patient=patient_profile.objects.all()
           # return render(request,'admin_dashboard.html',{'head':head ,'info':info,'patient':patient})

        elif request.user.is_staff:
            return redirect('doctor_dashboard')

        else:
            return redirect('patient_dashboard')


def admin_dashboard(request):
    head = profile.objects.filter()
    info=doctor_profile.objects.all()
    patient=patient_profile.objects.all()
    appoint=appointment.objects.all()
    return render(request,'admin_dashboard.html',{'info':info ,'head':head ,'patient':patient,'appoint':appoint})


def hospital_head_profile(request):
    head = profile.objects.all()
    return render(request, 'hospital_head_profile.html', {'head': head})


def head_profile(request):
    if request.method=="POST":
        name = request.POST['fname']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        unicode = request.POST['unicode']
        country = request.POST['country']
        photo = request.FILES['photo']

        # dp = doctor_profile.objects.filter(us=request.user.id)
        #
        # dp.update(full_name=name, email=email, date_of_birth=date_of_birth,mobile_number=mobile, address=address)
        # dp.save()
        app=profile(fname=name, email=email, date_of_birth=date_of_birth,mobile=mobile, address=address, city=city, state=state, unicode=unicode, country=country, photo=photo)
        app.save()
        # head = profile.objects.all()
        # return render(request, 'hospital_head_profile.html', {'head': head})
        return redirect('admin_dashboard')


def doctor_register(request):
    return render(request,"doctor_register.html")

def  doc_reg(request):
    if request.method=="POST":
        full_name =request.POST['full_name']
        birth_date=request.POST['date_of_birth']
        gender=request.POST['gender']
        email = request.POST['email']
        mobile_number =request.POST['mobile_number']
        address = request.POST['address']
        specialization=request.POST['specialization']
        education=request.POST['education']
        password = request.POST['password']
        doctors=request.FILES['doctors']


        us = User.objects.create_user(username=email,password=password,first_name=full_name,email=email,is_staff=True)
        us.save()

        app=doctor_profile(full_name=full_name, date_of_birth=birth_date,gender=gender,mobile_number=mobile_number,
                   email=email,address=address,specialization=specialization,education=education,doctors=doctors,us=us)
        app.save()
        #return HttpResponse("successfull")
        return redirect('admin_dashboard')


def admin_doctor_list(request):
    head = profile.objects.filter()
    info=doctor_profile.objects.all()
    patient=patient_profile.objects.all()
    appoint = appointment.objects.all()
    return render(request,"admin_doctor_list.html",{'info':info ,'head':head ,'patient':patient,'appoint':appoint})

def admin_appointment_list(request):
    head = profile.objects.filter()
    info = doctor_profile.objects.all()
    patient = patient_profile.objects.all()
    appoint = appointment.objects.all()
    return render(request,"admin_appointment_list.html",{'info':info ,'head':head ,'patient':patient,'appoint':appoint})

def doctor_dashboard(request):
    data = doctor_profile.objects.filter(us=request.user)
    doctor_name = request.user.first_name
    appoint = appointment.objects.filter(doctor_name=doctor_name)
    return render(request, "doctor_dashboard.html", {'data': data,'appoint':appoint})

# def doctor_profile_setting(request):
#     data = doctor_profile.objects.filter(us=request.user)
#     return render(request,"doctor_profile_setting.html",{'data': data})

# def update_doctor_profile(request):
#     if request.method == "POST":
#         full_name = request.POST['full_name']
#         birth_date = request.POST['date_of_birth']
#         gender = request.POST['gender']
#         email = request.POST['email']
#         mobile_number = request.POST['mobile_number']
#         address = request.POST['address']
#         specialization = request.POST['specialization']
#         education = request.POST['education']
#         doctors = request.FILES['doctors']
#
#         doctor_profile.objects.filter(us=request.user).update(full_name=full_name, date_of_birth=birth_date,gender=gender,mobile_number=mobile_number,
#                    email=email,address=address,specialization=specialization,education=education,doctors=doctors)
#         return redirect('doctor_dashboard')




def patient_dashboard(request):
    result = patient_profile.objects.filter(us=request.user)
    patient_name = request.user.first_name
    appoint = appointment.objects.filter(patient_name=patient_name)
    return render(request, "patient_dashboard.html", {'result': result,'appoint':appoint})


def patient_register(request):
    return render(request,"patient_register.html")

def  patient_reg(request):
    if request.method=="POST":
        full_name =request.POST['full_name']
        birth_date=request.POST['date_of_birth']
        email = request.POST['email']
        mobile_number =request.POST['mobile_number']
        address = request.POST['address']
        password = request.POST['password']
        patients=request.FILES['patients']

        us= User.objects.create_user(username=email,password=password,first_name=full_name,email=email)
        us.save()

        app=patient_profile(full_name=full_name, date_of_birth=birth_date,mobile_number=mobile_number,
                   email=email,address=address,patients=patients,us=us)
        app.save()
        return redirect('login')


def schedule_timing(request):
    return render(request,"schedule_timing.html")


def booking(request):
    docdata = doctor_profile.objects.all()
    return render(request,'appointment_book.html', {'bookmod': docdata})


def search_doctor(request):
    if request.method=="POST":
        gender=request.POST.get('gender')
        specialization=request.POST.get('specialization')
        docsearch=doctor_profile.objects.filter(gender=gender,specialization=specialization)
        return render(request,'appointment_book.html',{'bookmod':docsearch})
    else:
        docdata=doctor_profile.objects.all()
        return render(request,'appointment_book.html',{'bookmod':docdata})

def select_doctor(request):
            dr_id = request.GET['id']
            doctor_name=request.GET['full_name']
            #dr_name =doctor_profile.objects.filter(full_name=full_name)
            patient_name=request.user.first_name
            pt_id=request.user.id
#            app=appointment.objects.create(dr_id=dr_id,pt_id=pt_id,patient_name=patient_name,doctor_name=doctor_name)
#            app.save()
            bdata=doctor_profile.objects.all().filter(id=dr_id)
            return render(request,'book_slot.html',{'bdata':bdata})

def book_slot(request):
    if request.method == "POST":
        appt_date = request.POST['appt_date']
        time_slot= request.POST['time_slot']
        dr = request.POST['id']
        doctor_name = doctor_profile.objects.get(id=dr).full_name
        app=appointment(dr_id=dr,pt_id=request.user.id,appt_date=appt_date,time_slot=time_slot,patient_name=request.user.first_name,doctor_name=doctor_name)
        app.save()
        return HttpResponse("appointment is booked")
        # return render(request,'book_slot.html')


def fetch_appointment(request):
    if request.method == "POST":
        dr_id=request.POST['dr_id']
        appt_date=request.POST['appt_date']
        print(dr_id,appt_date)
        data=appointment.objects.all().filter(dr_id=dr_id,appt_date=appt_date)
        return HttpResponse("success")

def log_out(request):
    logout(request)
    return redirect("/")

def reset_password(request):
    #print(request.user.first_name)
    if request.method=='POST':
        email=request.POST['email']
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        us=authenticate(username=email,password=oldpassword)
        if us is not None:
            us.set_password(newpassword)
            us.save()
            return render(request,'login.html')
        else:
            print('Username password not found')
        print(us)
    return render(request,'change_password.html')






