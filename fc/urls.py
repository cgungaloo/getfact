from django.urls import path
from django.conf.urls import url
from . import views	
from django.contrib.auth import views as auth_views
from django.conf.urls import include

# Put urls in order for page matching

urlpatterns =[
	url(r'^$',views.home,name='home'),
	url(r'^fc/new/$',views.fc_new,name='fc_new'),
	url(r'^fc/(?P<pk>\d+)/edit/$',views.fc_edit,name='fc_edit'),
	url(r'^fc_detail/(?P<pk>\d+)/$',views.fc_detail, name='fc_detail'),
	url(r'^fc/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^likefact/$', views.likeFact, name='likeFact'),
	url(r'^dislikefact/$', views.dislikeFact, name='dislikeFact'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('accounts/',include('django.contrib.auth.urls'))
]