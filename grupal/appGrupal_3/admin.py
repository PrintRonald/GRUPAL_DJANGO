from django.contrib import admin
from .models import Cliente
from .models import Contacto
from .models import productos
from .models import Profile
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(productos)
admin.site.register(Profile)


