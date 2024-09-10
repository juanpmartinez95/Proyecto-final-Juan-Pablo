from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.CustomLoginView.as_view(), name="login"), 
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("edit_profile/", views.edit_profile, name="edit_profile"), 
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)