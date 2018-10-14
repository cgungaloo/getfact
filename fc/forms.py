from django import forms

from .models import Fact,Comment

class FcForm(forms.ModelForm):

    class Meta:
        model = Fact
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'text',)