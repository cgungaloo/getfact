from django import forms

from .models import Fact,Comment,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FcForm(forms.ModelForm):

    class Meta:
        model = Fact
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)

class ImageUploadForm(forms.Form):
	image = forms.ImageField()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user