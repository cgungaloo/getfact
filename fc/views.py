from django.shortcuts import render, get_object_or_404
from .models import Fact, Comment, LikeDislike
from django.utils import timezone
from .forms import FcForm, CommentForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
import json

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

@login_required
def likeFact(request):

	fc_id = None
	fc=None
	if request.method == 'GET':
		fc_id = request.GET['fc_id']
		fc = get_object_or_404(Fact, pk=fc_id)
	try:
		likedislike = LikeDislike.objects.get(fcId=fc_id,user=request.user)
		if likedislike.vote == -1:
			likedislike.vote =1
			likedislike.save()
			fc.totalLikes +=1
			fc.totalDislikes -=1
			fc.save()
		print("Got LikeDislike")
	except LikeDislike.DoesNotExist:
		print("DoesNotExist")
		likedislike = LikeDislike(vote=1, user=request.user,fcId=fc)
		fc.totalLikes +=1
		fc.save()
		likedislike.save()

	likesdata ={'likes':fc.totalLikes,'dislikes': fc.totalDislikes} 
	return HttpResponse(json.dumps(likesdata))

@login_required
def dislikeFact(request):

	fc_id = None
	fc=None
	if request.method == 'GET':
		fc_id = request.GET['fc_id']
		fc = get_object_or_404(Fact, pk=fc_id)
	try:
		likedislike = LikeDislike.objects.get(fcId=fc_id,user=request.user)
		print(likedislike.vote)
		if likedislike.vote == 1:
			likedislike.vote = -1
			likedislike.save()
			fc.totalLikes -=1
			fc.totalDislikes +=1
			fc.save()
		print("Got LikeDislike")
	except LikeDislike.DoesNotExist:
		print("DoesNotExist")
		likedislike = LikeDislike(vote=1, user=request.user,fcId=fc)
		fc.totalDislikes +=1
		fc.save()
		likedislike.save()

	likesdata ={'likes':fc.totalLikes,'dislikes': fc.totalDislikes}

	return HttpResponse(json.dumps(likesdata))

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'