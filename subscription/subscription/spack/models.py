from django.db import models

PACK_CHOICES = [
    ('499','basic'),
    ('599', 'premium'),
    ('699', 'vip'),
    ('799','vvip'),
    ('899','live pack')
]



# Create your models here.
class User(models.Model):
    mobile=models.BigIntegerField()
    smc=models.CharField(max_length=20,unique=True)
    price=models.IntegerField(choices=PACK_CHOICES,null=True,blank=True)
    pack=models.CharField(max_length=50,null=True,blank=True)
    objects = models.Manager()
