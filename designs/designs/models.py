from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import models
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['username',
                  'password',

                  'email',
                  ]
        # fields = '__all__


# null for backend(sql)
# blank for front-end
# default ha false no need to assign true only we have to assign
class user(models.Model):
    u_name = models.CharField(max_length=100)
    u_email = models.EmailField(max_length=100)
    s_phone = models.BigIntegerField(null=True, blank=False)
    s_address = models.CharField(max_length=200)
    manager = models.Manager()


class designs(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=500)
    manager = models.Manager()
