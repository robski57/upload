from django.conf.urls import url
from index import views
urlpatterns = [
url(r'^form/$', views.form),
url(r'^upload/$', views.Upload)

]
