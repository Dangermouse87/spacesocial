from django.contrib import admin
from . import models

# Register your models here.

class GroupMemberInline(admin.TabularInline): # allows admin to look at group members through group and edit those too.
    model = models.GroupMember

admin.site.register(models.Group)
