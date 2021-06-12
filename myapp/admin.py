from django.contrib import admin

# Register your models here.
from myapp import models as mp
admin.site.register(mp.contact)
admin.site.register(mp.Register)
admin.site.register(mp.diseases)
admin.site.register(mp.clinics)
admin.site.register(mp.patient)
admin.site.register(mp.doctor)
admin.site.register(mp.labs)
admin.site.register(mp.Message)
admin.site.register(mp.hospital)
admin.site.register(mp.blogs)
admin.site.register(mp.helpandsupport)
admin.site.register(mp.appointment_table)





