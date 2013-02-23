from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	email = models.CharField(max_length=200)
	zip_code = models.IntegerField()
	phone_number = models.CharField(max_length=20)

class Request(models.Model):
	user = models.ForeignKey(User)
	item = models.CharField(max_length=300)

class Status(models.Model):
    BUSY = 'B'
    AVAILABLE = 'A'
    HIDDEN = 'H'
    STATUS_CHOICES = ((BUSY, 'busy'),(AVAILABLE, 'available'),(HIDDEN, 'hidden'))
    user = models.ForeignKey(User)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=AVAILABLE)

