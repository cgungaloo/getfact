from django.contrib import admin
from .models import Fact, Comment,LikeDislike

admin.site.register(Fact)
admin.site.register(Comment)
admin.site.register(LikeDislike)
