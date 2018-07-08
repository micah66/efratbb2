from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schedule', views.schedule, name='schedule'),
    url(r'^standings', views.standings, name='standings'),
    url(r'^register', views.register, name='register'),
    url(r'^comments', views.comments, name='comments'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^contacts', views.contacts, name='contacts'),
]
