from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    birthday = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
