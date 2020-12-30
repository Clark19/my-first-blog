from django.contrib import admin
from .models import Post, Comment

# Admin 패널에 모델을 등록
admin.site.register(Post)
admin.site.register(Comment)