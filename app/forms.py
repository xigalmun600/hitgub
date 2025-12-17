from django import forms
from .models import Repository, Collaborate, User


class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ["owner", "name", "description", "is_private"]
        labels = {
            "name": "Repository name",
            "description": "Description",
            "is_private": "Is it private?",
            "owner": "Owner (Select User)",
        }


class NewUserForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(), label="Confirm password"
    )

    class Meta:
        model = User
        fields = ["name", "email", "password"]
        widgets = {
            "password": forms.PasswordInput(),
        }

    def clean(self):
        clean = super().clean()

        password = clean.get("password")
        password_confirm = clean.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error(
                "password_confirm",
                "Passwords do not match. Idiot.",
            )
        return clean
