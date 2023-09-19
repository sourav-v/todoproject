
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    # path('details', views.details, name='details')
    path('delete/<int:taskid>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update, name='update'),
    path('cbvhome/', views.TaskListview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Updateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Deleteview.as_view(), name='cbvdelete')
]