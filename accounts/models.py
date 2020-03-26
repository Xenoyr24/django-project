from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image


class GuestEmail(models.Model):
	email      = models.EmailField()
	active      = models.BooleanField(default=True)
	updated     = models.DateTimeField(auto_now=True)
	timestamp   = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email


DISTRICT_CHOICES = (
    ('Port Louis','Port-Louis'),
    ('Flacq','Flacq'),
    ('Grand Port','Grand Port'),
    ('Moka','Moka'),
    ('Plaines Wilhems','Plaines Wilhems'),
    ('Riviere du Rempart','Riviere du Rempart'),
    ('Riviere Noire','Riviere Noire'),
    ('Savanne','Savanne'),
    ('Pamplemousses','Pamplemousses')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    other_name = models.CharField(max_length=100, default='', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    district  = models.CharField(default='Port Louis',max_length=120, choices=DISTRICT_CHOICES)
    bio = models.TextField(max_length=500, blank=True)
    phone = models.IntegerField(default=0, blank=True)
    email_confirmed = models.BooleanField(default=False)

    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

