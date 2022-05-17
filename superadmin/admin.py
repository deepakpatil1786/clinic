from django.contrib import admin

# Register your models here.
from superadmin.models import*

@admin.register(User)
class User(admin.ModelAdmin):
    list_display =['name','email','password','role','clinic','gender','speciality',]


@admin.register(SLOT)
class SLOT(admin.ModelAdmin):
    list_display =['id','doctor','timeslot','weekslot',]
    

@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display =['slot','patient_id','patient_name','weekslot','timeslot','date',]