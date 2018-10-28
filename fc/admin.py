from django.contrib import admin
from .models import Fact, Comment,LikeDislike,Profile,ReviewComment

admin.site.register(Fact)
admin.site.register(Comment)
admin.site.register(LikeDislike)
admin.site.register(Profile)
admin.site.register(ReviewComment)
