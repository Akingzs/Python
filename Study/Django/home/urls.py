from django.urls import path
from . import views as home_view

urlpatterns = [
    path('', home_view.home),
    path('page1/', home_view.page1),
    path('page2/', home_view.page2),
    path('page3/', home_view.page3)
]
