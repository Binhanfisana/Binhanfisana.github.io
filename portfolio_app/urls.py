from django.urls import path

from .views import about, contact, home, projects

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', about, name='about'),
    path('projetos/', projects, name='projects'),
    path('contato/', contact, name='contact'),
]
