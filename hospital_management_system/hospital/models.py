from django.db import models

# Create your models here.
departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

blood_groups=[
    ('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),
    ('AB+','AB+'),('AB-','AB-')
]
class doctor(models.Model):
    name=models.CharField(max_length=225)
    phone=models.BigIntegerField()
    email=models.EmailField()
    address=models.TextField()
    qualification=models.CharField(max_length=225)
    department=models.CharField(max_length=50,choices=departments)

    def __str__(self):
        return self.name

class patient(models.Model):
    name=models.CharField(max_length=225)
    phone=models.BigIntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')])
    age=models.IntegerField()
    blood_group=models.CharField(max_length=5,choices=blood_groups)
    weight=models.IntegerField()
    symptoms=models.CharField(max_length=100)
    doctorName=models.ForeignKey(doctor,on_delete=models.CASCADE,null=True)
    admitDate=models.DateField(auto_now=True)
    

    def __str__(self):
        return self.name

class appointment(models.Model):
    name=models.CharField(max_length=225)
    phone=models.BigIntegerField()
    email=models.EmailField()
    symptoms=models.CharField(max_length=100)
    doctorName=models.ForeignKey(doctor,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return self.name

class PatientDischargeDetails(models.Model):
    name=models.CharField(max_length=40)
    phone = models.BigIntegerField(null=True)
    email=models.EmailField()
    address = models.CharField(max_length=255)
    gender=models.CharField(max_length=10,choices=[('Male','Male'),('Female','Female')])
    age=models.IntegerField()
    blood_group=models.CharField(max_length=5,choices=blood_groups)
    weight=models.IntegerField()
    symptoms = models.CharField(max_length=100,null=True)
    doctorName=models.CharField(max_length=40)
    ailment = models.CharField(max_length=255)
    medicine = models.TextField()

    

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    
    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.patientName