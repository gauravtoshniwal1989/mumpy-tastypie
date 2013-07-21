from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.serializers import Serializer
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication, BasicAuthentication, ApiKeyAuthentication, SessionAuthentication, DigestAuthentication, OAuthAuthentication

from todo.models import Todo, UserTodo
from django.contrib.auth.models import User
from todo.api.auth import CustomAuthentication

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
		ordering=['todo'] # Specify the field names on which ordering is allowed
		resource_name = 'user_todo'
		fields = ['todo', 'user','due']
		filtering = {
			'todo':ALL,
			'due':ALL,
			'created':ALL,
			'done':ALL,
			'user':ALL_WITH_RELATIONS
		}
		serializer = Serializer(formats=['json'])
		authorization = Authorization()
		# authentication = BasicAuthentication()
		# authentication = SessionAuthentication()
		# authentication = ApiKeyAuthentication()
		authentication = CustomAuthentication()