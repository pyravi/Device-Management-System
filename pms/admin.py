from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import (TblSettings,
                     TblCountry, TblCurency, TblDepartment, TblEmployeetechnologies,
                     TblEmployees, TblFlag, TblHolidays, TblLockedresource, TblTechnologies, TblUser, TblUserlog,
                     TblUsertype
                    )


class TblUserAdmin(admin.ModelAdmin):
    list_display = ['userid',
                    'firstname',
                    'lastname',
                    'accountemail',
                    'accountphone',
                    'usertype',
                    'password',
                    'isactive',
                    'deleted',
                    'usercode',
                    'status',
                    'deptid',
                    'managerid',
                    'exempttimesheet',
                    'createddate',
                    'uan',
                    'pan',
                    'lastlogin',
                    'imageurl',
                    'timesheetcounter']


class TblUsertypeAdmin(admin.ModelAdmin):
    list_display = ['usertypeid', 'usertype']


class TblUserlogAdmin(admin.ModelAdmin):
    list_display = ['userid',
                    'logindate',
                    'logintime',
                    'logouttime',
                    'workingminutes',
                    'isactive',
                    'createddate',
                    'modifieddate'
                    ]


class TblTechnologiesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'status',
    ]


class TblSettingsAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'value',
                    'isactive',
                    'created',
                    'modified',
                    ]


class TblCountryAdmin(admin.ModelAdmin):
    list_display = ['countryid', 'name']


class TblCurencyAdmin(admin.ModelAdmin):
    list_display = ['curuncyid', 'curuncyname']


class TblDepartmentAdmin(admin.ModelAdmin):
    list_display = ['departmentname', 'status']


class TblEmployeetechnologiesAdmin(admin.ModelAdmin):
    list_display = ['etid', 'empid', 'techid']


class TblEmployeesAdmin(admin.ModelAdmin):
    list_display = ['empid',
                    'empname',
                    'roleid',
                    'loginid',
                    'password',
                    'status',
                    'empcode',
                    ]
    search_fields = ('empname',)


class TblFlagAdmin(admin.ModelAdmin):
    list_display = ['flagid', 'flagimagepath']


class TblHolidaysAdmin(admin.ModelAdmin):
    list_display = [
        'holidaydate',
        'occasionname',
        'isactive',
        'datecreated',
        'datemodified',
    ]


class TblLockedresourceAdmin(admin.ModelAdmin):
    list_display = [
        'lid',
        'userid',
        'lockeddate',
        'lockedby',
        'unlockeddate',
        'unlockedby',
    ]

# admin.site.register(TblCountry, TblCountryAdmin)
# admin.site.register(TblCurency, TblCurencyAdmin)
# admin.site.register(TblDepartment, TblDepartmentAdmin)
# admin.site.register(TblEmployeetechnologies, TblEmployeetechnologiesAdmin)
# admin.site.register(TblEmployees, TblEmployeesAdmin)
# admin.site.register(TblFlag, TblFlagAdmin)
# admin.site.register(TblHolidays, TblHolidaysAdmin)
# admin.site.register(TblLockedresource, TblLockedresourceAdmin)
# admin.site.register(TblTechnologies, TblTechnologiesAdmin)
# admin.site.register(TblUser, TblUserAdmin)
# admin.site.register(TblUserlog, TblUserlogAdmin)
# admin.site.register(TblUsertype, TblUsertypeAdmin)
# admin.site.register(TblSettings, TblSettingsAdmin)

