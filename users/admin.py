from django.contrib import admin
from .models import profile
# Register your models here.

admin.site.register(profile)







# if we import from model class like profile(from .models import profile), and use admin.site.register(profile) , and now we go to admin url entering id pass we can saw there new option created profile. we did also same in blog/admin.py