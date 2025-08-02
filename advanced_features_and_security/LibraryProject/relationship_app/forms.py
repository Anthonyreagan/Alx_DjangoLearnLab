from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User # Still remove this
from django.contrib.auth import get_user_model # <--- NEW IMPORT!
# from django.conf import settings # No longer strictly needed for 'model = ...'

from .models import Book # Assuming Book is still in the same forms.py context

# Get the custom user model once
CustomUser = get_user_model() # <--- GET THE ACTUAL MODEL CLASS HERE!

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Use the actual model class object here
        model = CustomUser # <--- CHANGE THIS!

        # Explicitly list the fields for your CustomUser.
        # UserCreationForm.Meta.fields already includes password1 and password2.
        # So you just need to list your additional fields and 'email'.
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'profile_photo') + UserCreationForm.Meta.fields

    # If you have custom save logic or specific field widgets, keep them here
    def save(self, commit=True):
        user = super().save(commit=False)
        if 'profile_photo' in self.cleaned_data:
            user.profile_photo = self.cleaned_data['profile_photo']
        if commit:
            user.save()
        return user


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']