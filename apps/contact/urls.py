from django.urls import path
from apps.contact import views


urlpatterns = [
    path('contact',views.contact,name='contact'),

    path("dashboard/", views.contact_messages, name="contact_dashboard"),
    path("dashboard/<int:pk>/", views.contact_detail, name="contact_detail"),
    path('toggle-read/<int:pk>/', views.toggle_read, name='toggle_read'),
]