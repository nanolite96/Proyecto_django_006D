from django.conf.urls import url
from rest_framework import urlpatterns
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/trabajos/$',views.TrabajosViewSet.as_view()),
    url(r'^api/contactos/$',views.ContactoViewSet.as_view()),
    url(r'^api/trabajo_crear/$',views.TrabajosCreateViewSet.as_view()),
    url(r'^api/contactos_crear/$',views.ContactoCreateViewSet.as_view()),
    url(r'^api/trabajo/(?P<nombre>.+)/$',views.TrabajoBuscarViewSet.as_view()),
    url(r'^api/contacto/(?P<nombre_cl>.+)/$',views.ContactoBuscarViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)