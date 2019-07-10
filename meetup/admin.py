from django.contrib import admin
from django.contrib.auth.models import Group as Group2



# Register your models here.
from django.contrib.auth.admin import UserAdmin

from meetup.forms import RegisterForm
from meetup.models import *


class group_admin(admin.ModelAdmin):
    list_display = ('name','group_id','creator','category','photo')
    search_fields = ('name','group_id','creator','category')
    list_filter = ('name','group_id','creator','category')
    ordering = ('name',)

admin.site.register(Group,group_admin)

class meetup_admin(admin.ModelAdmin):
    list_display = ('name','meetup_id','host','group','photo','fee')
    search_fields = ('name','meetup_id','host','group')
    list_filter = ('name','meetup_id','host','group')
    ordering = ('name',)

admin.site.register(Meetup,meetup_admin)

class user_admin(UserAdmin):

    add_form = RegisterForm

    list_display = ('email', 'user_id', 'host', 'staff','admin','photo')
    search_fields = ('email', 'user_id', 'host', 'staff','admin')
    list_filter = ('email', 'user_id', 'host')
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','host','staff','interests','photo')}),
        ('Permissions', {'fields': ('admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

admin.site.register(User,user_admin)
# admin.site.register(UserManager)
admin.site.register(Interest)
admin.site.register(GroupMemberDetails)
admin.site.register(MeetupMemberDetails)
admin.site.unregister(Group2)

