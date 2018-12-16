from django.contrib import admin
from .models import UserRegister
from .models import Contact
from .models import payment


from .models import Cancel


# Register your models here.
class UserRegisteradmin(admin.ModelAdmin):
    list_display = ['fname','email_id','contact_no']
    class meta:
        model=UserRegister


admin.site.register(UserRegister,UserRegisteradmin)
admin.site.register(Contact)
admin.site.register(payment)

admin.site.register(Cancel)