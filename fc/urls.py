from django.urls import path
from django.conf.urls import url
from . import views	
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

# Put urls in order for page matching

urlpatterns =[
	url(r'^$',views.home,name='home'),
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
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('accounts/',include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)