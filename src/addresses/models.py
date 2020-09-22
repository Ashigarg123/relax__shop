from django.db import models
from billing.models import BillingProfile
# Create your models here.

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=120, choices=(('shipping', 'shipping'), ('billing', 'billing')))
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True,blank=True)
    city = models.CharField(max_length=120)
    country= models.CharField(max_length=120, choices=(('India', 'India'), ('U.S','U.S'),('Africa','Africa')) ,default='India')
    state = models.CharField(max_length=120)
    Postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{line1}\n{line2}\n{city}\n{country}\n{state}\n{postal_code}\n".format(line1= self.address_line_1,
        line2=self.address_line_2,
        city=self.city,
        country=self.country,
        state=self.state,
        postal_code=self.Postal_code)
