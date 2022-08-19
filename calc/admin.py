from django.contrib import admin
from .models import data
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(data)
class PersonAdmin(ImportExportModelAdmin):
    list_diaplay=('code','type','name','branch1','semester1 ','branch2','semester2 ','branch3','semester3','classroom_code1','classroom_code2','classroom_code3','faculty1','faculty2','faculty3','theory','tutorial','lab','lab_name')



