from django import template
from dms.models import Request_manager,Device_manager,Device_allocation_manager
register = template.Library()


@register.simple_tag
def dashboard_data():
    device_count = Device_manager.objects.count()
    request_count = Request_manager.objects.count()
    device_allocation_count = Device_allocation_manager.objects.count()
    context = [device_count, request_count, device_allocation_count]
    return context
