from django import forms
from .models import Request_manager,Device_allocation_manager,Device_manager
from pms.models import TblUser
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.forms import TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RequestFrom(forms.ModelForm):
    class Meta:
        model = Request_manager
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RequestFrom, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['till_date'].widget = TextInput(attrs={
            'id': 'date',
            'placeholder': "MM/DD/YYYY",
            'class': 'fa fa-calendar'
        })
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean_email(self):
        Email = self.cleaned_data.get('email')
        try:
            email_qs = TblUser.objects.get(accountemail=Email)
            return Email
        except ObjectDoesNotExist:
            raise forms.ValidationError("Your Email ID does not exist")



class Device_allocation_ManagerForm(forms.ModelForm):
    class Meta:
        model = Device_allocation_manager
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Device_allocation_ManagerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['till_date'].widget = TextInput(attrs={
            'id': 'date',
            'placeholder': "MM/DD/YYYY",
            'class': 'fa fa-calendar'
        })
        self.helper.add_input(Submit('submit', 'Submit'))


class Device_ManagerForm(forms.ModelForm):
    class Meta:
        model = Device_manager
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Device_ManagerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['purchased'].widget = TextInput(attrs={
            'id': 'date',
            'placeholder': "MM/DD/YYYY",
            'class': 'fa fa-calendar'
        })
        self.helper.add_input(Submit('submit', 'Submit'))