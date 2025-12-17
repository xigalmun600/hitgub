from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class User(models.Model):
    profile_picture = models.ImageField(upload_to="profiles/", null=True, blank=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    collaborate = models.ManyToManyField("Repository", through="Collaborate")
    follow = models.ManyToManyField("self", symmetrical=False, related_name="followers")

    def clean(self):
        if self.name == self.password:
            raise ValidationError(
                {"password": "The name and the password cannot be the same"}
            )
        super().clean()

    def __str__(self):
        return f"{self.name}"


class Repository(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="repositories"
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Collaborate(models.Model):
    class PermissionChoices(models.TextChoices):
        READ = "RD", "Read"
        WRITE = "WR", "Write"
        ADMIN = "AR", "Admin"

    permissions = models.CharField(
        max_length=2, choices=PermissionChoices.choices, default=PermissionChoices.READ
    )
    repo = models.ForeignKey(
        Repository, on_delete=models.CASCADE, related_name="collaborations"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="collaborators"
    )

    def __str__(self):
        return f"{self.user.name} - {self.repo.name} ({self.permissions})"
