from django.db import models

class Profile(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER = (
        (MALE, 'Male'), (FEMALE, 'Female'),
    )
    profile_code    = models.CharField(max_length=15)
    last_name       = models.CharField(max_length=30)
    first_name      = models.CharField(max_length=30)
    middle_name     = models.CharField(max_length=30)
    birth_date       = models.DateField(auto_now=False)
    gender          = models.CharField(max_length=6, choices=GENDER, default=MALE)
    home_address    = models.CharField(max_length=254)




