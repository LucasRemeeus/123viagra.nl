from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    BioText = models.TextField()
    City = models.TextField()
    DateOfBirth = models.DateField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Medicine(models.Model):
    Name = models.TextField()
    Manufacturer = models.TextField()
    Cures = models.TextField()
    SideEffects = models.TextField()

    def __str__(self):
        return self.Name


class Collection(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(null=True, blank=True)
    Collected = models.BooleanField(default=False)
    CollectedApproved = models.BooleanField(default=False)
    CollectedApprovedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="CollectedApprovedBy")

    def __str__(self):
        return f"{self.user.get_username()} - {self.Medicine.Name}"
