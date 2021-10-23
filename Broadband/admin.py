from django.contrib import admin
from.models import Login,Customer_Reg,Worker_Reg,Plans_Reg,Admin_Request,Customer_complaints



# Register your models here.
admin.site.register(Login)
admin.site.register(Customer_Reg)
admin.site.register(Worker_Reg)
admin.site.register(Plans_Reg)
admin.site.register(Admin_Request)
admin.site.register(Customer_complaints)


