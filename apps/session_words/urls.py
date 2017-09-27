from django.conf.urls import url
from . import views

print "in project urls"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^clear$', views.clear),

]