from django.contrib import admin
from scan.models import *
# Register your models here.



admin.site.register(ROLES)

class EmployeesAdmin(admin.ModelAdmin) :
         pass

    
admin.site.register(Employee,EmployeesAdmin)
admin.site.register(CompanyOutlet)
admin.site.register(AccessToken)

admin.site.register(ActivityEmployee)


