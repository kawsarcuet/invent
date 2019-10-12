from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item) is done
@admin.register(Desktops, Laptops, Mobiles)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
              hello my

              i am lucky to go here
hg















