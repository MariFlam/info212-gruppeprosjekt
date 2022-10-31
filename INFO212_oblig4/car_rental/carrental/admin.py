from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Car, Customer, Employee


class CarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)
