from django.contrib import admin
from .models import Job
from .models import User
from .models import Contact
from .models import Hiring
from .models import Applicant
admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Hiring)
admin.site.register(User)

admin.site.register(Contact)

