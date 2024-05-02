from django.contrib import admin

# Register your models here.
from web.models import Data,Founder,Contact,Job,Apply
admin.site.register(Data)
admin.site.register(Founder)
admin.site.register(Contact)
admin.site.register(Job)
admin.site.register(Apply)