from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_html, name='hello_html'),
    path('hello/<str:name>', views.hello_name, name='hello_name'),
    path('hello_query', views.hello_query, name='hello_query'),
    path('special', views.special_view, name='special_view'),
    #path('postview', views.post_view, name='post_view'),
    #path('submitpost', views.submit_post, name='submit_post'),
    #path('submitdjangopost', views.submit_django_post, name='submit_django_post'), 
    path('templateview',views.template_view,name='template_view'),
    path('todosview',views.todos_view,name='todos_view'),
    path('person/<int:person_id>',views.person_details,name='person_details'),
    path('deletetodos/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('toggletododone/<int:todo_id>/', views.toggle_todo_done, name='toggle_todo_done')
]
