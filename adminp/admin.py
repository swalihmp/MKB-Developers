from django.contrib import admin
from .models import Property,Photos,Amenities,Contact

# Register your models here.

admin.site.register(Property)
admin.site.register(Photos)
admin.site.register(Amenities)
admin.site.register(Contact)