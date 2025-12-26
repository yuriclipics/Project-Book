from django.urls import path
from .views import pages, AboutPageView

urlpatterns = [
    path("aboutpageview/", AboutPageView.as_view(), name="about_page_view"),
    path("", pages, name="pages_home"),
]
