from django.contrib import admin
from .models import Video, Comment_Model,ReplyModel, Rating
# Register your models here.
admin.site.register(Video)
admin.site.register(Comment_Model)
admin.site.register(ReplyModel)
admin.site.register(Rating)