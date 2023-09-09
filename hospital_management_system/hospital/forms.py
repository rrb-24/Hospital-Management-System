from django import forms
from django.forms import ModelForm
from .models import patient,doctor,appointment,PatientDischargeDetails

class patientForm(ModelForm):
    class Meta:
        model = patient
        fields = "__all__"
        labels={
            'name':'',
            'phone':'',
            'email':'',
            'gender':'',
            'age':'',
            'blood_group':'',
            'weight':'',
            'symptoms':'',
            'doctorName':'',
            'admitDate':'',
        }

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'gender':forms.Select(attrs={'class':'form-select','placeholder':'Gender'}),
            'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Age'}),
            'blood_group':forms.Select(attrs={'class':'form-select','placeholder':'Blood Group'}),
            'weight':forms.NumberInput(attrs={'class':'form-control','placeholder':'Weight'}),
            'symptoms':forms.TextInput(attrs={'class':'form-control','placeholder':'Symptoms'}),
            'doctorName':forms.Select(attrs={'class':'form-select','placeholder':'Doctor Name','selected':'Name'}),
        }

class doctorForm(ModelForm):
    class Meta:
        model = doctor
        fields = "__all__"

        labels={
            'name':'',
            'phone':'',
            'email':'',
            'address':'',
            'qualification':'',
            'department':'',
        }

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'qualification':forms.TextInput(attrs={'class':'form-control','placeholder':'Qualification'}),
            'department':forms.Select(attrs={'class':'form-select','placeholder':'Department'}),
        }

class appointmentForm(ModelForm):
    class Meta:
        model = appointment
        fields = "__all__"

        labels={
            'name':'',
            'phone':'',
            'email':'',
            'symptoms':'',
            'doctorName':'',
            'date':'',
        }

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'symptoms':forms.TextInput(attrs={'class':'form-control','placeholder':'Symptoms'}),
            'doctorName':forms.Select(attrs={'class':'form-select','placeholder':'Doctor Name'}),
            'date':forms.DateInput(attrs={'class':'form-control','placeholder':'Appointment Date YYYY-MM-DD'}),
        }

class PatientDischargeForm(ModelForm):
    class Meta:
        model = PatientDischargeDetails
        fields=('name','phone','email','address','gender','age','blood_group'
                ,'weight','symptoms','doctorName','ailment','medicine','roomCharge'
                ,'medicineCost','doctorFee','OtherCharge')
        
        labels={
            'name':'',
            'phone':'',
            'email':'',
            'address':'',
            'gender':'',
            'age':'',
            'blood_group':'',
            'weight':'',
            'symptoms':'',
            'doctorName':'',
            'ailment':'',
            'medicine':'',
            'roomCharge':'',
            'medicineCost':'',
            'doctorFee':'',
            'OtherCharge':'',
        }

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Patient Name'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone Number','id':'phone'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','id':'email'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'gender':forms.Select(attrs={'class':'form-select','id':'gender'}),
            'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Age','id':'age'}),
            'blood_group':forms.Select(attrs={'class':'form-select','id':'blood_group'}),
            'weight':forms.NumberInput(attrs={'class':'form-control','placeholder':'Weight','id':'weight'}),
            'symptoms':forms.TextInput(attrs={'class':'form-control'}),
            'doctorName':forms.TextInput(attrs={'class':'form-control'}),
            'ailment':forms.TextInput(attrs={'class':'form-control','placeholder':'Ailment'}),
            'medicine':forms.TextInput(attrs={'class':'form-control','placeholder':'Medicine'}),
            'roomCharge':forms.NumberInput(attrs={'class':'form-control','placeholder':'Room Charge','id':'room'}),
            'medicineCost':forms.NumberInput(attrs={'class':'form-control','placeholder':'Medicine Cost','id':'med'}),
            'doctorFee':forms.NumberInput(attrs={'class':'form-control','placeholder':'Doctor Fee','id':'doc'}),
            'OtherCharge':forms.NumberInput(attrs={'class':'form-control','placeholder':'Other Charges','id':'other'}),
        }