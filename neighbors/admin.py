from django.contrib import admin
from neighbors.models import User, Request, Status

admin.site.register(User)
admin.site.register(Request)
admin.site.register(Status)