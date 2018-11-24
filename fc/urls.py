from django.urls import path
from django.conf.urls import url
from . import views	
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
	LoginView,
	LogoutView,
	PasswordResetView,
	PasswordResetDoneView,
	PasswordChangeView,
	PasswordChangeDoneView,
	PasswordResetConfirmView,
	PasswordResetCompleteView
	)

from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

# Put urls in order for page matching

urlpatterns =[
	url(r'^$',views.home,name='home'),
	url(r'myfacts',views.myfacts,name='myfacts'),
	url(r'mycomments',views.mycomments,name='mycomments'),
	url(r'deleteaccount',views.deleteaccount,name='deleteaccount'),
	url(r'myaccount/',views.myaccount,name='myaccount'),
	url(r'search/',views.search,name='search'),
	url(r'^myaccount/upload_profile_pic',views.upload_pic,name='upload_pic'),
	url(r'^fc/new/$',views.fc_new,name='fc_new'),
	url(r'^fc/(?P<pk>\d+)/edit/$',views.fc_edit,name='fc_edit'),
	url(r'^fc/(?P<pk>\d+)/delete/$',views.fc_delete,name='fc_delete'),
	url(r'^fc_detail/(?P<pk>\d+)/$',views.fc_detail, name='fc_detail'),
	url(r'^fc/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^fc/(?P<pk>\d+)/comment_delete/(?P<fpk>\d+)/$', views.delete_comment, name='delete_comment'),
	url(r'^likefact/$', views.likeFact, name='likeFact'),
	url(r'^dislikefact/$', views.dislikeFact, name='dislikeFact'),
	url(r'^truecomment/$', views.trueComment, name='trueComment'),
	url(r'^falsecomment/$', views.falseComment, name='falseComment'),
	url(r'^sortofcomment/$', views.sortOfComment, name='sortOfComment'),
	url(r'^login/$',LoginView.as_view(template_name='registration/login.html'),name='login'),
	url(r'^logout/$',LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
	url(r'^password_change/$',PasswordChangeView.as_view(template_name='registration/password_change_form.html'),name='password_change'),
    url(r'^password_change/done/$',PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),name='password_change_done'),
	url(r'^password_reset/$',PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
	url(r'^password_reset/done/$',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
	url(r'^reset/done/$',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
	# url('^', include('django.contrib.auth.urls')),
	path('signup/', views.SignUp.as_view(), name='signup'),
	# path('accounts/',include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)