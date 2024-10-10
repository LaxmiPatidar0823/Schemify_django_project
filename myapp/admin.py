from django.contrib import admin
from myapp.models import Userdata
from myapp.models import SchemeData

# Register your models here.

class userModel(admin.ModelAdmin):
    list_display = ('user_name','user_age', 'user_category','user_state','user_annualincome', 'user_profession', 'user_gender' )
    
admin.site.register(Userdata, userModel)


class schemeModel(admin.ModelAdmin):
    list_display = ('scheme_name','scheme_caste','scheme_annualIncome','scheme_gender','scheme_age','scheme_Minage','scheme_education_level','scheme_benefits')
    
admin.site.register(SchemeData,schemeModel)
