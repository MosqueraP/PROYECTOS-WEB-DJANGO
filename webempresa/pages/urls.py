from django.urls import path
from pages import views

urlpatterns = [
    path("<int:page_id>/", views.page, name='page'),
]
