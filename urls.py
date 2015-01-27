from django.conf.urls import patterns, url

from site_flow import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^about/', views.AboutView.as_view(), name="about"),
    url(r'^faq/', views.FaqView.as_view(), name="faq"),
#    url(r'^contact/', views.ContactView.as_view(), name="contact"),
)
