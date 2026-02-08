from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# FOR REST FRAMEWORK
# from rest_framework import routers
# from djangowithfastapipydantic.views import MovieViewSet, ActionViewSet

# REST FRAMEWORK ROUTER USED FOR SERIALIZERS
#eg1 : localhost:8000/movies/
# router = routers.SimpleRouter()
# router.register('movies', MovieViewSet)

# router = routers.SimpleRouter()
# router.register('movies', MovieViewSet, basename='movies')
# router.register('actions', ActionViewSet, basename='actions')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('todo.urls')),
    path('', include('mysite.urls')),
    path('users/',include('users.urls')),
    #path('', include('djangowithfastapipydantic.urls')), # Not needed as we are using router for REST framework so use when normal django views are used
    #path('', include(router.urls)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)