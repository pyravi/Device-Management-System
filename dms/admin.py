from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from django.contrib.auth import get_user_model
from .models import (
    Device_manager,
    Images,
    Device_allocation_manager,
    Request_manager,
    Dashboard,
    EmailBackend,
    )

from django.db.models import Count

class DeviceInfoImageInline(admin.TabularInline):
    model = Images
    extra = 1

class DeviceInfoAdmin(admin.ModelAdmin):
    list_display = ['image_tag','model_name',
                    'mobile_company_name',
                    'color',
                    'extra_accessories',
                    'description',
                    'device_type',
                    ]
    inlines = [DeviceInfoImageInline]
    readonly_fields = ('image_tag',)

class Device_allocationAdmin(admin.ModelAdmin):
    list_display=['assign_employee',
        'assign_device',
        'description',
        'created_date',
                ]
    search_fields=('assign_employee__empname','assign_device__model_name',)

class RequestmanagerAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'assign_device',
        'description',
        'till_date'
    ]


@admin.register(Dashboard)
class DeviceManagementAdmin(admin.ModelAdmin):
    change_list_template = 'admin/dashboard.html'

    # def get_context_data(self, **kwargs):
    #     context = super(DeviceManagementAdmin, self).get_context_data(**kwargs)
    #     some_data = Device_manager.objects.all()
    #     context.update({'some_data': some_data})
    #     return context
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # qs = request_list.objects.all()
        # qs = device_allocation.objects.all()
        return qs
    # def get_osm_info(self):
    #     qs = Device_manager.objects.all()
    #     print(qs)
    #     return qs


    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(request,extra_context=extra_context,)
    #     response['device_list']=Dashboard.objects.all().count()
    #     return response

admin.site.register(Device_manager,DeviceInfoAdmin)
admin.site.register(Device_allocation_manager,Device_allocationAdmin)
admin.site.register(Request_manager,RequestmanagerAdmin)

#####Remove Recent Action logs
# from django.contrib.admin.models import LogEntry

# # LogEntry.objects.all().delete()
