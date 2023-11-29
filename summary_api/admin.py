from django.contrib import admin
from .models import Summary, UserVideoSummary

# Register your models here.
admin.site.register(Summary)
admin.site.register(UserVideoSummary)