from django.contrib import admin

from .models import patient,doctor,appointment,PatientDischargeDetails
# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(appointment)
admin.site.register(PatientDischargeDetails)
