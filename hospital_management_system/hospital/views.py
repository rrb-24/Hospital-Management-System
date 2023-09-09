from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import patient,doctor,appointment,PatientDischargeDetails
from .forms import patientForm,doctorForm,appointmentForm,PatientDischargeForm
from datetime import date

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def admin_login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password,is_staff=True)
        if user is not None:
            login(request,user)
            return redirect('admin_panal')
        else:
            print('invalid')
    else:
        print('2 invaild')
    return render(request,'admin_login.html')

def admin_panal(request):
    current_user=request.user
    # print(current_user)
    user_details=User.objects.get(username=current_user)
    patients_count=patient.objects.count()
    doctors_count=doctor.objects.count()
    app_count=appointment.objects.count()
    todays_app=appointment.objects.filter(date=date.today()).values()
    # docID=appointment.objects.filter(date=date.today()).values('doctorName_id')
    # print(docID)
    # lists=[]
    # for i in docID:
    #     doc=doctor.objects.values('name')
    #     if docID==doc:
    #         lists.append(doc)
    # # print(appointment.objects.)

    # print(lists)
    # print(User.objects.filter(username=current_user).values())
    return render(request,'admin_panal.html',{'user_details':user_details,
    'pat_count':patients_count,'doc_count':doctors_count,'app_count':app_count,'tod_app':todays_app})

def logout(request):
    currentUser=request.user
    logout(currentUser)
    return redirect('admin_login')

def patients_list(request):
    patients=patient.objects.all()
    patients_count=patient.objects.count()
    return render(request,'patients_list.html',{'patients':patients,'patients_count':patients_count})

def add_patient(request):
    # submitted=False
    if request.method=="POST":
        form = patientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    form = patientForm
    return render(request,'add_patient.html',{'form':form})

def view_edit_patient(request,patient_id):
    patient_info=patient.objects.get(id=patient_id)
    form = patientForm(request.POST or None,instance=patient_info)
    if form.is_valid():
        form.save()
        return redirect('patients_list')
    # return redirect('patients_list')
    return render(request,'view_edit_patient.html',{'form':form})

def patient_discharge(request,patient_id):
    patient_info=patient.objects.get(id=patient_id)
    # lists=[patient_info.name,patient_info.phone,patient_info.email,patient_info.gender,patient_info.age
    # ,patient_info.blood_group,patient_info.weight,patient_info.doctorName.name,patient_info.symptoms]
    # print(lists)
    context={'name':patient_info.name,'phone':patient_info.phone,'email':patient_info.email,'gender':patient_info.gender,
    'age':patient_info.age,'blood_group':patient_info.blood_group,'weight':patient_info.weight,'doctorName':patient_info.doctorName.name,
    'symptoms':patient_info.symptoms,'id':patient_id}
    # form = PatientDischargeForm(request.POST or None, instance=patient_info)
    # if form.is_valid():
    #     form.save()
    #     return redirect('bill')
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        gender=request.POST['gender']
        age=request.POST['age']
        blood_group=request.POST['blood_group']
        weight=request.POST['weight']
        symptoms=request.POST['symptoms']
        doctorName=request.POST['doctorName']
        ailment=request.POST['ailment']
        medicine=request.POST['medicine']
        room=int(request.POST['room'])
        med=int(request.POST['med'])
        doc=int(request.POST['doc'])
        other=int(request.POST['other'])
        admitDate=patient_info.admitDate
        dischargeDate=date.today()
        daysSpend=dischargeDate-admitDate
        daySpent=daysSpend.days
        total=room+med+doc+other
        # print(patient_info.admitDate)
        dataSave=PatientDischargeDetails.objects.create(name=name,phone=phone,email=email,address=address,gender=gender,
        age=age,blood_group=blood_group,weight=weight,symptoms=symptoms,doctorName=doctorName,ailment=ailment,medicine=medicine,roomCharge=room,
        medicineCost=med,doctorFee=doc,OtherCharge=other,total=total,daySpent=daySpent,admitDate=admitDate,releaseDate=dischargeDate)
        dataSave.save()
        return render(request,'bill.html',{'data':dataSave})

    return render(request,'patient_discharge.html',context)
#{'form':form,'patient_info':lists}

def delete_patient(request,patient_id):
    get_pat=patient.objects.get(id=patient_id)
    get_pat.delete()
    patients=patient.objects.all()
    patients_count=patient.objects.count()
    return render(request,'patients_list.html',{'patients':patients,'patients_count':patients_count})

def doctors_list(request):
    doctors=doctor.objects.all()
    doctors_count=doctor.objects.count()
    return render(request,'doctors_list.html',{'doctors':doctors,'doctors_count':doctors_count})

def add_doctor(request):
    # submitted=False
    if request.method=="POST":
        form = doctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors_list')
    form = doctorForm
    return render(request,'add_doctor.html',{'form':form})

def view_edit_doctor(request,doctor_id):
    doctor_info=doctor.objects.get(id=doctor_id)
    form = doctorForm(request.POST or None,instance=doctor_info)
    if form.is_valid():
        form.save()
        return redirect('doctors_list')
    # return redirect('doctors_list')
    return render(request,'view_edit_doctor.html',{'form':form})

def delete_doctor(request,doctor_id):
    get_doc=doctor.objects.get(id=doctor_id)
    get_doc.delete()
    doctors=doctor.objects.all()
    doctors_count=doctor.objects.count()
    return render(request,'doctors_list.html',{'doctors':doctors,'doctors_count':doctors_count})

def appointments(request):
    appointmentss=appointment.objects.all()
    app_count=appointment.objects.count()
    return render(request,'appointments.html',{'appointments':appointmentss,'app_count':app_count})

def create_appointment(request):
    if request.method=="POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    form = appointmentForm
    return render(request,'create_appointment.html',{'form':form})

def create__appointment(request):
    if request.method=="POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_confirm')
    form = appointmentForm
    return render(request,'create__appointment.html',{'form':form})

def App_confirm(request):
    return render(request,'confirm_app.html')

def cancel_appointment(request,app_id):
    get_app=appointment.objects.get(id=app_id)
    get_app.delete()
    appointmentss=appointment.objects.all()
    app_count=appointment.objects.count()
    return render(request,'appointments.html',{'appointments':appointmentss,'app_count':app_count})

def check_app(request):
    if request.method=="POST":
        phone=request.POST['phone']
        pat_details=appointment.objects.filter(phone=phone).values()
        if pat_details!=None:
            return render(request,'check_app.html',{'pat_details':pat_details})
        
    return render(request,'check_app.html')

def cancel__appointment(request,app_id):
    get_app=appointment.objects.get(id=app_id)
    
    try:
        phone=appointment.objects.get(phone=get_app.phone)
    except:
        pass
    get_app.delete()
    appointmentss=appointment.objects.filter(phone=phone.phone).values()
    return render(request,'check_app.html',{'pat_details':appointmentss})

def bill(request):
    
    print(id)
    return render(request,'bill.html')