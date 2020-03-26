from django.db import models

from billing.models import BillingProfile
from django.core.urlresolvers import reverse

ADD_CHOICE = u'Billing address'
ADDRESS_TYPES = (
    ('billing', u'Billing address'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES, default=ADD_CHOICE)
    #name            = models.CharField(max_length=120, null=True, blank=True, help_text='Shipping to? Who is it for?')
    #nickname        = models.CharField(max_length=120, null=True, blank=True, help_text='Internal Reference Nickname')
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='United States of America')
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        if self.nickname:
            return str(self.nickname)
        return str(self.address_line_1)

    def get_absolute_url(self):
        return reverse("address-update", kwargs={"pk": self.pk})


    def get_address(self):
        return "{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
                #for_name = self.name or "",
                line1 = self.address_line_1,
                line2 = self.address_line_2 or "",
                city = self.city,
                state = self.state,
                postal= self.postal_code,
                country = self.country
            )

