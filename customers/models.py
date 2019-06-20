from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

# Create your models h

LITRES = (
    ('40Ltrs', '40Ltrs'),
    ('60Ltrs', '60Ltrs'),
    ('80Ltrs', '80Ltrs'),
    ('100Ltrs', '100Ltrs'),
    ('120Ltrs', '120Ltrs'),
    ('140Ltrs', '140Ltrs'),
    ('160Ltrs', '160Ltrs'),
    ('180Ltrs', '180Ltrs'),
    ('200Ltrs', '200Ltrs'),

)
class customer(models.Model):
    name = models.CharField(max_length =100, )
    Street_address= models.CharField(max_length=120)
    Litres= models.CharField(max_length=120, choices=LITRES, default='40Ltrs')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateTimeField(default=now)

    def __str__(self):
            return self.name