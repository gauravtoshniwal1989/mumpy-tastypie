from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.serializers import Serializer
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication, BasicAuthentication, ApiKeyAuthentication, SessionAuthentication, DigestAuthentication, OAuthAuthentication

from todo.models import Todo, UserTodo
from django.contrib.auth.models import User
from todo.api.auth import CustomAuthentication, UserObjectsOnlyAuthorization
from django.db.models import Q
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
	todo_lower = fields.CharField()
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
		
		# authentication = BasicAuthentication()
		# authentication = SessionAuthentication()
		# authentication = ApiKeyAuthentication()
		# authentication = CustomAuthentication()

		# authorization = Authorization()
		authorization = UserObjectsOnlyAuthorization()

	def apply_filters(self, request, applicable_filters):
		base_object_list = super(UserTodoResource, self).apply_filters(request, applicable_filters)
		query = request.GET.get('query', None)
		ids = request.GET.get('ids', None)
		filters = {}
		# if ids:
		# 	ids = ids.replace('+', ' ').split(' ')
		# 	filters.update(dict(id__in=ids))
		if query:
			qset = (
				Q(todo__icontains=query, **filters)
				# |
				# Q(description__icontains=query, **filters)
			)
			base_object_list = base_object_list.filter(qset).distinct()
		return base_object_list.filter(**filters).distinct()
	def dehydrate_todo(self, bundle):
		return bundle.data['todo'].upper()
	def dehydrate(self, bundle):
		bundle.data['todo_lower'] = bundle.data['todo'].lower()
		return bundle