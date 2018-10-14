from django.shortcuts import render, get_object_or_404
from .models import Fact, Comment
from django.utils import timezone
from .forms import FcForm, CommentForm
from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def home(request):
	facts = Fact.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

	return render(request, 'home.html',{'facts':facts})

def fc_detail(request,pk):
	print("In FC Detail#############")
	fc = get_object_or_404(Fact, pk=pk)
	return render(request, 'fc_detail.html', {'fc': fc})

def fc_new(request):
	if request.method == "POST":
		form = FcForm(request.POST)
		if form.is_valid():
			fc = form.save(commit=False)
			fc.author = request.user
			fc.published_date = timezone.now()
			fc.save()
			return redirect('fc_detail', pk=fc.pk)
	else:
		form = FcForm()
	return render(request, 'fc_edit.html',{'form':form})

def fc_edit(request,pk):
	fc = get_object_or_404(Fact, pk=pk)
	if request.method == "POST":
		form =FcForm(request.POST, instance = fc)
		if form.is_valid():
			fc = form.save(commit=False)
			fc.author = request.user
			fc.published_date = timezone.now()
			fc.save()
			return redirect('fc_detail', pk=fc.pk)
	else:
		form = FcForm(instance=fc)
	return render(request,'fc_edit.html',{'form':form})

def add_comment_to_post(request,pk):
	fc = get_object_or_404(Fact, pk=pk)
	if request.method =="POST":
		form =CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.comment = fc
			comment.save()
			return redirect('fc_detail',pk=fc.pk)
	else:
		form =CommentForm()
	return render(request,'add_comment_to_post.html',{'form':form})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'