from django import forms

from .models import Fact,Comment,Profile

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