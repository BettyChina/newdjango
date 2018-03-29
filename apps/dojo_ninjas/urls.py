from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ="index"),
    url(r'^main$', views.register, name = "register"),
    url(r'^quotes$', views.success, name = "success"),
    url(r'^login$', views.login, name = "login"),
    url(r'^create$', views.create, name = "create"),
    url(r'^addtolist$', views.addtolist, name = "addtolist"),
    url(r'^update$', views.update, name = "update"),
    url(r'^logout$', views.logout, name = "logout")
   
]

#from django.conf.urls import url
#from . import views           # This line is new!
#urlpatterns = [
   
  #   url(r'^$', views.index),     # This line has changed!
  #   url(r'^users/sucess$', views.users/success),     # This line has changed!
  #  url(r'^process_money$', views.process_money)
  #  url(r'^create$', views.create),
  #  url(r'^(?P<number>\d+)$', views.show),
  #  url(r'^(?P<number>\d+)/edit$', views.edit),
  #  url(r'^(?P<number>\d+)/delete$', vi
  #]

