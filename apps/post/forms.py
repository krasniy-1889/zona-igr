from django.contrib import admin
from django.contrib.auth import get_user_model
from django import forms

from .models import Comment


class CommentModelAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].initial = self.request.user
