import imp
from random import choices
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from superadmin.models import SLOT, Appointment, User
# from django.contrib.auth.decorators import login_required
from datetime import date


# Create your views here.
# @login_required
def index(request):
    admin_profile = User.objects.get(email=request.session['email'])
    uid = User.objects.get(email=request.session['email'])
    return render(request, 'index.html', {'uid': uid, 'admin_profile': admin_profile})


def index_doctor(request):
    # admin_profile=User.objects.get(email=request.session['email'])
    doc_profile = User.objects.get(email=request.session['email'])
    uid = User.objects.get(email=request.session['email'])
    return render(request, 'index-doctor.html', {'uid': uid, 'doc_profile': doc_profile})


def index_patient(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request, 'index-patient.html', {'uid': uid})


def login(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "admin":
            return redirect('index')
        elif uid.role == "doctor":
            return redirect('index-doctor')
        else:
            return redirect('index-patient')
    except:
        if request.method == "POST":
            try:
                uid = User.objects.get(email=request.POST['email'])
                if uid.role == "admin":
                    if request.POST['password'] == uid.password:
                        request.session['email'] = request.POST['email']
                        return redirect('index')
                    return render(request, 'login.html', {'msg': 'enter a valid password'})

                elif uid.role == "doctor":
                    if request.POST['password'] == uid.password:
                        request.session['email'] = request.POST['email']
                        return redirect('index-doctor')
                    return render(request, 'login.html', {'msg': 'enter a valid password'})

                else:
                    if request.POST['password'] == uid.password:
                        request.session['email'] = request.POST['email']
                        return redirect('index-patient')
                    return render(request, 'login.html', {'msg': 'enter a valid password'})
            except:
                msg = "please enter valid email"
                return render(request, 'login.html', {'msg': msg})
    return render(request, 'login.html')


def logout(request):
    del request.session['email']
    return redirect('login')

   # ---- DOCTOR -----#

def Create_doctor(request):
    admin_profile = User.objects.get(email=request.session['email'])

    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Doctor Email is already Exits "
            return render(request,'create-doctor.html',{'msg':msg,'admin_profile':admin_profile})
        except:
            password = ''.join( choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            subject = "welcom to hospital"
            message = f"""Hello {request.POST['name']},
            Your Username is  {request.POST['email']},
            Your Password is {password} """
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail(subject, message, email_form, recipient_list)
            User.objects.create(
                role=request.POST['role'],
                name=request.POST['name'],
                email=request.POST['email'],
                password=password,
            )
            msg1 ='DOCTOR IS CREATED'
        return render(request, 'create-doctor.html',{'msg1':msg1,'admin_profile':admin_profile})

    return render(request, 'create-doctor.html', {'admin_profile': admin_profile})


def view_doctor(request):
    doc_profile = User.objects.get(email=request.session['email'])
    admin_profile = User.objects.get(email=request.session['email'])

    uid = User.objects.all().filter(role='doctor')
    return render(request, 'view-doctor.html', {'uid': uid, 'doc_profile': doc_profile, 'admin_profile': admin_profile})


def update_doctor(request, pk):
    uid = User.objects.get(id=pk)
    admin_profile = User.objects.get(email=request.session['email'])

    doc_profile = User.objects.get(email=request.session['email'])

    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.clinic = request.POST['clinic']
        uid.gender = request.POST['gender']
        uid.speciality = request.POST['speciality']
        uid.Address = request.POST['Address']
        uid.save()
    return render(request, 'update-doctor.html', {'uid': uid, 'doc_profile': doc_profile, 'admin_profile': admin_profile})


def delete_doctor(request, pk):
    doctor = User.objects.get(id=pk)
    doctor.delete()
    return redirect('view-doctor')


def profile_doctor(request):

    uid = User.objects.get(email=request.session['email'])
    doc_profile = User.objects.get(email=request.session['email'])

    if request.method == "POST":
        uid.name = request.POST['name']
        uid.clinic = request.POST['clinic']
        uid.gender = request.POST['gender']
        uid.speciality = request.POST['speciality']
        uid.Address = request.POST['Address']
        uid.save()
    return render(request, 'profile-doctor.html', {'uid': uid, 'doc_profile': doc_profile})


#----patient---#


def create_patient(request):
    admin_profile = User.objects.get(email=request.session['email'])

    if request.method == "POST":
       try:
            User.objects.get(email=request.POST['email'])
            msg = "Patient Email is already Exits "
            return render(request,'create-patient.html',{'msg':msg,'admin_profile':admin_profile})
       except:
            password = ' '.join(
             choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
            subject = 'welcom to hospital'
            message = f"""Hello {request.POST['name']},
            Your Username is  {request.POST['email']},
            Your Password is {password} """
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail(subject, message, email_form, recipient_list)
            User.objects.create(
                role=request.POST['role'],
                name=request.POST['name'],
                email=request.POST['email'],
                password=password,
            )
            msg1= 'PATIENT IS CREATED'
       return render(request, 'create-patient.html', {'msg':msg1,'admin_profile':admin_profile})

    return render(request, 'create-patient.html', {'admin_profile': admin_profile})


def view_patient(request):
    admin_profile = User.objects.get(email=request.session['email'])

    uid = User.objects.all().filter(role='patient')
    return render(request, 'view-patient.html', {'uid': uid, 'admin_profile': admin_profile})


def update_patient(request, pk):
    admin_profile = User.objects.get(email=request.session['email'])

    uid = User.objects.get(id=pk)
    if request.method == 'POST':
        uid.name = request.POST['name']

        uid.gender = request.POST['gender']
        if 'profile' in request.FILES:
            uid.profile = request.FILES['profile']
        uid.save()
    return render(request, 'update-patient.html', {'uid': uid, 'admin_profile': admin_profile})


def delete_patient(request, pk):
    patient = User.objects.get(id=pk)
    patient.delete()
    return redirect('view-patient')


def profile_patient(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        uid.name = request.POST['name']
        uid.gender = request.POST['gender']
        uid.Address = request.POST['Address']
        if 'profile' in request.FILES:
            uid.profile = request.FILES['profile']

        uid.save()

    return render(request, 'profile-patient.html', {'uid': uid})

   #----SLOT--#


def slot(request):
    doc_profile = User.objects.get(email=request.session['email'])

    data = User.objects.get(email = request.session['email'])
    uid = SLOT.objects.filter(doctor__id = data.id)
    if request.method == 'POST':
        uid2 = SLOT.objects.filter(doctor__id = data.id,timeslot=int(request.POST['timeslot']),weekslot=int(request.POST['weekslot'])).exists()

        if uid2:
            msg ='slot is already available'
            return render(request,'slot.html',{'msg':'slot is already available'})
        else:
                SLOT.objects.create(
                    doctor = data,
                    weekslot = request.POST['weekslot'],
                    timeslot = request.POST['timeslot']
                )
                msg = "Slot Added Sucessfully"
        return render(request,'slot.html',{'msg':msg,'doc_profile':doc_profile})
    return render(request,'slot.html',{'doc_profile':doc_profile})



def view_slot(request):
    doc_profile = User.objects.get(email=request.session['email'])
    var = User.objects.get(email=request.session['email'])
    uid = SLOT.objects.all().order_by('doctor')
    return render(request, 'view-slot.html', {'uid': uid, 'var': var, 'doc_profile': doc_profile})


def update_slot(request, pk):

    uid = SLOT.objects.get(id=pk)
    doc_profile = User.objects.get(email=request.session['email'])

    if request.method == 'POST':
        uid.timeslot = request.POST['timeslot']
        uid.weekslot = request.POST['weekslot']
        uid.save()
        # return redirect('update-slot')
    return render(request, 'update-slot.html', {'uid': uid, 'doc_profile': doc_profile})


def delete_slot(request, pk):
    slot = SLOT.objects.get(id=pk)
    slot.delete()
    return redirect('view-slot')


   #------appointment-------#

def book_appointment(request):
    uid = User.objects.get(email=request.session['email'])
    book = User.objects.filter(role='doctor')
    # app = Appoinment.objects.all()
    slot = SLOT.objects.all().order_by('weekslot')
    f_id = []
    for i in slot:
        a = Appointment.objects.filter(slot=i)
        for a1 in a:
            f_id.append(a1.slot.id)
    # print(f_id,'===============')
    final_slot = SLOT.objects.all().exclude(id__in=f_id).order_by('weekslot')
    # print(final_slot,'---------------final_slot---------------------')
    return render(request,'book-appointment.html',{'book':book,'slot':slot,'uid':uid})



def create_appointment(request):
                               # doc_v = request.GET.get("doc_v")
    pat = User.objects.get(email=request.session['email'])
    # print(getslot)
    if request.method == "POST":
        
        getslot = SLOT.objects.get(weekslot=request.POST['weekslot'],timeslot=request.POST['timeslot'],doctor__id=request.POST['doctor_name'])
        Appointment.objects.create(
            slot=getslot,
            patient_id=pat.id,
            patient_name=pat.name,
            weekslot=request.POST['weekslot'],  
            timeslot=request.POST['timeslot'],
            decription=request.POST['decription'],
            date = request.POST['date'],
        )
    return redirect('book-appointment')


def get_slot_list(request):
    temp = User.objects.get(email = request.session['email'])
    week_n = request.GET.get("week_n")
    doc_v = request.GET.get("doc_v")
    slot1 = SLOT.objects.filter(weekslot = week_n).filter(doctor=doc_v).order_by('timeslot').values('id','timeslot')
    # print(temp.id,'===========')
    booked_app = []
    app = Appointment.objects.filter(patient_id=temp.id)
    for i in app:
        booked_app.append(i.slot.id)
    # print(booked_app,'----------')
    final_slot = SLOT.objects.filter(doctor = request.GET.get("doc_n")).exclude(id__in=booked_app).order_by('weekslot').values('id','weekslot')
    # print(final_slot,'---------------final_slot---------------------')
    return JsonResponse({
        "instances" : list(final_slot),
        "instances1" : list(slot1)
    })


def view_appointment(request):  #-----view--patient---#
    uid = User.objects.get(email=request.session['email'])
    var1 = Appointment.objects.filter(patient_id=uid.id)
    return render(request,'view-appointment',{'uid':uid,'var1':var1})




def view_appointment_admin(request):  #-----view-appointment-to-admin-#
    admin_profile = User.objects.get(email=request.session['email'])

    uid = User.objects.get(email=request.session['email'])
    app1= Appointment.objects.all()

    return render(request,'view-appointment-admin.html',{'uid':uid,'app1':app1,'admin_profile':admin_profile})



def view_appointment_doc(request):#---views appointment to doctor--#
    day = date.today()
    doc_profile = User.objects.get(email=request.session['email'])

    uid=User.objects.get(email=request.session['email'])
    app2 =Appointment.objects.filter(slot__doctor=uid.id)
    return render(request,'view-appointment-doc.html',{'uid':uid,'app2':app2,'doc_profile':doc_profile,'day':day})




def status_complete(request,pk):
    uid=Appointment.objects.get(id=pk)
    uid.status = 1
    uid.save()
    return redirect('view-appointment-doc')

def status_absent(request,pk):
    uid=Appointment.objects.get(id=pk)
    uid.status= 2
    uid.save()
    return redirect('view-appointment-doc')


def status_cancel(request,pk):
    uid=Appointment.objects.get(id=pk)
    uid.status = 3
    uid.save()
    return redirect('view-appointment-doc')