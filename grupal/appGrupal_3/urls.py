from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.home, name='home'),
    path('registro', views.registro, name='registro'),
    path('contacto',views.contacto, name="contacto"),
    path('login/', LoginView.as_view(template_name='appGrupal_3/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='appGrupal_3/logout.html'), name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 