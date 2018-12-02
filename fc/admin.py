from django.contrib import admin
from .models import Fact, Comment,LikeDislike,Profile,ReviewComment,ReportFact,ReportComment


class FactAdmin(admin.ModelAdmin):
    list_display = ['id','author','title', 'text','created_date','published_date','totalLikes','totalDislikes']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author','comment', 'text','created_date','totalTrues','totalSortOfs','totalFalses']

class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ['id','vote','user', 'fcId']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

class ReviewComemntAdmin(admin.ModelAdmin):
	list_display =['id','vote','user']

class ReportFactAdmin(admin.ModelAdmin):
	list_display =['created_date','fact','investigated']

class ReportCommentAdmin(admin.ModelAdmin):
	list_display =['created_date','comment','investigated']


admin.site.register(Fact,FactAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(LikeDislike,LikeDislikeAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(ReviewComment,ReviewComemntAdmin)
admin.site.register(ReportFact,ReportFactAdmin)
admin.site.register(ReportComment)
