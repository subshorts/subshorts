from django.urls import path

from . import views

app_name = 'records'
urlpatterns = [
    path('', views.list_records, name='list'),
    path('export/', views.export_zone, name='zone_export'),
    path('import/', views.import_zone, name='zone_import'),
    path('create/', views.create_record, name='create'),
    path('<str:id>/', views.retrieve_record, name='detail'),
    path('<str:id>/update/', views.update_record, name='update'),
    path('<str:id>/delete/', views.delete_record, name='delete'),
]
