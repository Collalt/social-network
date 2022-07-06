from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class ProfileForm(forms.Form):
        avatar = forms.ImageField(label='avatar');
        bio = forms.CharField(label='bio', max_length=300)