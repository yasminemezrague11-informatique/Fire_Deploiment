from django.contrib import admin
from .models import FireIncident 
from .models import VehiculeDePompier
from .models import Pompier
from .models import Citoyen



# Register your models here.
admin.site.register(FireIncident)
admin.site.register(VehiculeDePompier)
admin.site.register(Pompier)
admin.site.register(Citoyen)

