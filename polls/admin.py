from django.contrib import admin

# Register your models here.
from polls.models import Person, AccessRecord
admin.site.register(AccessRecord)
admin.site.register(Person)