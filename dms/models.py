from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib import messages
# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


class Images(models.Model):
    device_image=models.ForeignKey("Device_manager", verbose_name=_("Device Image"), on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(_("Image"), upload_to='images/image', height_field=None, width_field=None, max_length=None,blank=True)

    def __str__(self):
        return self.title




class Device_manager(models.Model):
    device_choices = (
       ('A', 'Android'),
       ('I', 'IOS'),
       ('O', 'Other')
       )
    color_choices=(
            ( 'B','Black'),
            ('W','White'),
            ('G','Gold'),
            ('BU','Blue'),
            ('BR','Brown'),
            ('GR','Grey'),
            ('RG','Rose Gold'),
            ('MB','Matte Black'),
            ('GW','Gold White'),
            ('GB','Grey Black'),
            ('OT','Other Colour')
    )
    model_name= models.CharField(_("Mobile Name"), max_length=50)
    model_number= models.CharField(max_length=30,blank=True,null=True)
    mobile_company_name= models.CharField(max_length=150, blank=True, null=True)
    color = models.CharField(max_length=2, choices=color_choices)
    image = models.ImageField(_("Image"), upload_to='images', height_field=None, width_field=None, max_length=None,blank=False)
    extra_accessories = models.CharField(max_length=225,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    purchased=models.DateTimeField(_("Purchased Date"), auto_now=False, auto_now_add=False)
    device_type=models.CharField(max_length=1, choices=device_choices)

    class Meta:
        verbose_name = 'Device Manager'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.model_number

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse("dms:device")

class Device_allocation_manager(models.Model):
    assign_employee=models.ForeignKey("pms.TblUser", verbose_name=_("Assign Device Person Name"), on_delete=models.CASCADE,null=True, blank=True)
    assign_device=models.ForeignKey("Device_manager", verbose_name=_("Assign Device Name"), on_delete=models.CASCADE,null=True, blank=True)
    description=models.TextField(blank=True,null=True)
    till_date= models.DateTimeField(_("Till Date"), auto_now=False, auto_now_add=False)
    created_date =models.DateTimeField(_("Date"), auto_now=True)

    def __str__(self):
        return f'{self.assign_employee}' 

    class Meta:
        verbose_name = 'Device Allocation Manager'

    def get_absolute_url(self):
        return reverse("dms:device-assign")


class Request_manager(models.Model):
    email=models.EmailField(_("Requester Email Address"), max_length=254)
    assign_device=models.ForeignKey("Device_manager",verbose_name=_("Device Request or New Device"), on_delete=models.CASCADE,null=True, blank=True)
    description=models.TextField(blank=True,null=True)
    till_date= models.DateTimeField(_("Till Date"), auto_now=False, auto_now_add=False)
    created_date =models.DateTimeField(_("Request Created Date"), auto_now=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Request Manager'


    def get_absolute_url(self):
        return reverse("dms:request-page")

class Dashboard(models.Model):
    device_list = models.ForeignKey("Device_manager",
                                    verbose_name=_("Device Manager"),
                                    on_delete=models.CASCADE)
    request_list = models.ForeignKey("request_manager",
                                     verbose_name=_("Request Manager"),
                                     on_delete=models.CASCADE)
    device_allocation = models.ForeignKey("Device_allocation_manager",
                                          verbose_name=_("Device Allocation Manager"),
                                          on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Dashboard'
