from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from . import api

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    url(r'^index$', views.index, name='index'),
    url(r'^facts$', api.FactList.as_view(), name='facts'),
]
