from django.shortcuts import render, get_object_or_404
from .models import Fact, Comment, LikeDislike, User, ReviewComment,Profile
from django.utils import timezone
from .forms import FcForm, CommentForm, ImageUploadForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
import json

# Create your views here.
def home(request):
	facts = Fact.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'home.html',{'facts':facts})

@login_required
def myfacts(request):
	facts = Fact.objects.filter(author=request.user,published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'myfacts.html',{'facts':facts})

@login_required
def mycomments(request):
	comments = Comment.objects.filter(author=request.user).order_by('created_date')
	print(len(comments))
	return render(request, 'mycomments.html',{'comments':comments})

@login_required
def deleteaccount(request):
	try:
		Profile.objects.get(user=request.user).delete()
		User.objects.get(username=request.user.username).delete()
		facts = Fact.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		logout(request)
		return render(request, 'home.html',{'facts':facts})	
	except User.DoesNotExist:
		print("User does not exist")
		return(request,'myaccount.html')


@login_required
def myaccount(request):
	print('In myaccount')
	print("Trying to change image")
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			m = Profile.objects.get(user=request.user)
			m.image = form.cleaned_data['image']
			m.save()
	return render(request,'myaccount.html')

def fc_detail(request,pk):
	print("In FC Detail#############")
	fc = get_object_or_404(Fact, pk=pk)
	return render(request, 'fc_detail.html', {'fc': fc})

@login_required
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

@login_required
def add_comment_to_post(request,pk):
	fc = get_object_or_404(Fact, pk=pk)
	if request.method =="POST":
		form =CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.comment = fc
			comment.save()
			return redirect('fc_detail',pk=fc.pk)
	else:
		form =CommentForm()
	return render(request,'add_comment_to_post.html',{'form':form})

@login_required
def upload_pic(request):
	print("Trying to change image")
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			m = profile.objects.get(pk=request.user)
			m.image = form.cleaned_data['image']
			m.save()
			return HttpResponse('image upload success')
	return HttpResponseForbidden('allowed only via POST')

@login_required
def fc_delete(request,pk):
	fc = get_object_or_404(Fact, pk=pk)

	try:
		likesdislikeForFact = LikeDislike.objects.get(fcId=pk).delete()
	except LikeDislike.DoesNotExist:
		print("No likes or dislikes to delete for " + str(pk))

	try:
		commentsForFact= Comment.objects.get(comment=fc).delete()
	except Comment.DoesNotExist:
		print("No comments to delete for " + str(pk))

	fc.delete()
	facts = Fact.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'home.html',{'facts':facts})

@login_required
def delete_comment(request,pk,fpk):
	comment = Comment.objects.get(pk=pk)
	if comment.author == request.user:
		print("Deleting")
		comment.delete()
	return redirect('fc_detail',pk=fpk)


@login_required
def likeFact(request):
	print("Im in the view")
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
		likedislike = LikeDislike(vote=-1, user=request.user,fcId=fc)
		fc.totalDislikes +=1
		fc.save()
		likedislike.save()

	likesdata ={'likes':fc.totalLikes,'dislikes': fc.totalDislikes}

	return HttpResponse(json.dumps(likesdata))

@login_required
def trueComment(request):
	c_id = None
	comment = None
	if request.method == 'GET':
		c_id = request.GET['c_id']
		comment = get_object_or_404(Comment, pk=c_id)
	try:
		commentreview = ReviewComment.objects.get(comment=comment, user=request.user)
		if commentreview.vote == -1 or commentreview.vote ==0:
			if commentreview.vote ==0:
				comment.totalSortOfs -=1 
			if commentreview.vote == -1:
				comment.totalFalses -=1 
			commentreview.vote =1
			commentreview.save()
			comment.totalTrues +=1
			comment.save()
	except ReviewComment.DoesNotExist:
		commentreview = ReviewComment(vote=1,user=request.user,comment=comment)
		comment.totalTrues +=1
		comment.save()
		commentreview.save()

	commentReviewData ={'trues':comment.totalTrues,'sortofs': comment.totalSortOfs,'falses':comment.totalFalses}

	return HttpResponse(json.dumps(commentReviewData))

@login_required
def falseComment(request):
	c_id = None
	comment = None
	if request.method == 'GET':
		c_id = request.GET['c_id']
		comment = get_object_or_404(Comment, pk=c_id)

	print(comment)
	try:
		commentreview = ReviewComment.objects.get(comment=comment, user=request.user)
		print(str(commentreview.vote))
		if commentreview.vote == 1 or commentreview.vote ==0:
			print("Condition met")
			if commentreview.vote == 0:
				comment.totalSortOfs -=1 
			if commentreview.vote == 1:
				comment.totalTrues -=1 
			commentreview.vote = -1
			commentreview.save()
			comment.totalFalses +=1
			comment.save()
	except ReviewComment.DoesNotExist:
		commentreview = ReviewComment(vote=-1,user=request.user,comment=comment)
		comment.totalFalses +=1
		comment.save()
		commentreview.save()

	commentReviewData ={'trues':comment.totalTrues,'sortofs': comment.totalSortOfs,'falses':comment.totalFalses}

	return HttpResponse(json.dumps(commentReviewData))

@login_required
def sortOfComment(request):
	c_id = None
	comment = None
	if request.method == 'GET':
		c_id = request.GET['c_id']
		comment = get_object_or_404(Comment, pk=c_id)
	try:
		commentreview = ReviewComment.objects.get(comment=comment, user=request.user)
		if commentreview.vote == 1 or commentreview.vote == -1:
			if commentreview.vote == 1:
				comment.totalTrues -=1 
			if commentreview.vote == -1:
				comment.totalFalses -=1
			commentreview.vote = 0
			commentreview.save()
			comment.totalSortOfs +=1
			comment.save()

	except ReviewComment.DoesNotExist:
		commentreview = ReviewComment(vote=0,user=request.user,comment=comment)
		comment.totalSortOfs +=1
		comment.save()
		commentreview.save()

	commentReviewData ={'trues':comment.totalTrues,'sortofs': comment.totalSortOfs,'falses':comment.totalFalses}

	return HttpResponse(json.dumps(commentReviewData))

def password_reset(request):
	print("In Form")
	return render(request, 'registration/password_reset_form.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'