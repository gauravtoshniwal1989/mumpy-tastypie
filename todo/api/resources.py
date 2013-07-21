from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.serializers import Serializer
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from todo.models import Todo, UserTodo
from django.contrib.auth.models import User

class TodoResource(ModelResource):
	class Meta:
		queryset = Todo.objects.all()
		resource_name = 'todo'

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_superuser']
		serializer = Serializer(formats=['json'])


class UserTodoResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')
	class Meta:
		queryset = UserTodo.objects.all()
		resource_name = 'user_todo'
		fields = ['todo', 'user','due']
		serializer = Serializer(formats=['json'])
		authorization = Authorization()