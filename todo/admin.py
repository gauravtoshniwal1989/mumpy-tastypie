from django.contrib import admin
from todo.models import Todo, UserTodo

admin.site.register(Todo)
admin.site.register(UserTodo)