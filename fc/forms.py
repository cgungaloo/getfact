from django import forms

from .models import Fact,Comment,Profile, ReportFact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

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

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        self.clean()
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        user = self.cleaned_data.get('username')
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError("User Name already exists")
        return self.cleaned_data

class ReportFactForm(forms.ModelForm):
    class Meta:
        model =ReportFact
        fields =('reason',)
