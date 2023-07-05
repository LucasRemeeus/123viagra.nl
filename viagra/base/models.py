from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bioText = models.TextField()
    city = models.TextField()
    dateOfBirth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    cures = models.TextField()
    sideEffects = models.TextField()

    def __str__(self):
        return self.name


class Collection(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    collected = models.BooleanField(default=False)
    collectedApproved = models.BooleanField(default=False)
    collectedApprovedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                            related_name="CollectedApprovedBy")

    def __str__(self):
        return f"{self.user.get_username()} - {self.medicine.name}"
