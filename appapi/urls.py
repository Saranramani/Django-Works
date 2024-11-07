from django.urls import path
from . import views

urlpatterns = [
    path('getall/',views.getData),
    path('getbyid/<int:id>',views.getById),
    path('add/',views.addData),
    path('update/<int:id>',views.updateData),
    path('delete/<int:id>',views.deleteData),
]