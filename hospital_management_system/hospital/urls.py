from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_panal',views.admin_panal,name='admin_panal'),
    path('patients_list',views.patients_list,name='patients_list'),
    path('doctors_list',views.doctors_list,name='doctors_list'),
    path('appointments',views.appointments,name='appointments'),
    path('delete_patient/<patient_id>',views.delete_patient,name='delete_patient'),
    path('delete_doctor/<doctor_id>',views.delete_doctor,name='delete_doctor'),
    path('cancel_appointment/<app_id>',views.cancel_appointment,name='cancel_appointment'),
    path('cancel__appointment/<app_id>',views.cancel__appointment,name='cancel__appointment'),
    path('add_patient',views.add_patient,name='add_patient'),
    path('add_doctor',views.add_doctor,name='add_doctor'),
    path('create_appointment',views.create_appointment,name='create_appointment'),
    path('create__appointment',views.create__appointment,name='create__appointment'),
    path('view_edit_patient/<patient_id>',views.view_edit_patient,name='view_edit_patient'),
    path('view_edit_doctor/<doctor_id>',views.view_edit_doctor,name='view_edit_doctor'),
    path('bill',views.bill,name='bill'),
    path('App_confirm',views.App_confirm,name='App_confirm'),
    path('check_app',views.check_app,name='check_app'),
    path('patient_discharge/<patient_id>',views.patient_discharge,name='patient_discharge'),
]