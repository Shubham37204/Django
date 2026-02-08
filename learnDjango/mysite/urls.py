# Using Function Based Views
from django.urls import include, path
from . import views
# from django.views.decorators.cache import cache_page
app_name = 'mysite'

urlpatterns = [
    # path('',cache_page(60)( views.home), name='home'),
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.createItem, name='createItem'),
    path('update/<int:id>/edit/', views.edit_item, name='edit'),
    path('delete/<int:id>/', views.delete_item, name='delete'),
]


# Using Class Based Views
# from django.urls import path
# from .views import (
#     ItemListView,
#     ItemDetailView,
#     ItemCreateView,
#     ItemUpdateView,
#     ItemDeleteView,
# )

# app_name = 'mysite'

# urlpatterns = [
#     path('', ItemListView.as_view(), name='home'),
#     path('<int:pk>/', ItemDetailView.as_view(), name='detail'),
#     path('add/', ItemCreateView.as_view(), name='create'),
#     path('edit/<int:pk>/', ItemUpdateView.as_view(), name='edit'),
#     path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
# ]
