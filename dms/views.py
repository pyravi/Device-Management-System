from django.shortcuts import render,reverse
from django.http import HttpResponse
import requests,json
from django.views.generic import CreateView,View
from django.contrib.messages.views import SuccessMessageMixin
from .forms import (
    RequestFrom,
    Device_ManagerForm,
    Device_allocation_ManagerForm,
)

# Create your views here.
class AuthView(View):
    def get(self,*args, **kwargs):
        url = 'http://192.168.1.99:221/api/Login/Userlogin/'
        data = {'Email':'ravi.shanker@octalinfosolution.com', 'Password': 'octal@123'}
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        return HttpResponse(f'{r.text}')
    def post(self,*args, **kwargs):
        return HttpResponse('Authenticated')


class HomeView(SuccessMessageMixin,CreateView):
    form_class = RequestFrom
    template_name='request.html'
    success_message = '%(email)s request has been send!!!!'


class DeviceManagerView(SuccessMessageMixin,CreateView):
    form_class = Device_ManagerForm
    template_name='device_manager.html'
    success_message = '%(model_name)s device added !'


class DeviceAllocationView(SuccessMessageMixin, CreateView):
    form_class = Device_allocation_ManagerForm
    template_name='device_allocation.html'
    success_message = '%(assign_employee)s device allocated this person !'