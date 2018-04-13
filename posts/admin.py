from django.contrib import admin
from django.apps import apps

posts = apps.get_app_config('posts')

for model_name, model in posts.models.items():
    admin.site.register(model)
