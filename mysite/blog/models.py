from django.db import models
from django.contrib import admin

class BlogsPost(models.Model):
	title=models.CharField(max_length=150)
	body=models.TextField()
	timetamp=models.DateTimeField()
class BlogPostAdmin(admin.ModelAdmin):
	list_display=('title','timetamp')
admin.site.register(BlogsPost,BlogPostAdmin)
# Create your models here.
