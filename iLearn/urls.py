"""iLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from blog.views import article, index, AddReporterView, AddArticleView, ReporterList, About, AddContactView, \
    signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('article/', article, name="article"),
    path('reporter/', ReporterList, name="reporter"),
    path('add_reporter/', AddReporterView.as_view(), name="add_reporter"),
    path('add_article/', AddArticleView.as_view(), name="add_article"),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include('blog.urls')),
    path('about/', About, name="about"),
    path('contact_me/', AddContactView.as_view(), name='contact_me'),
    path('signup/', signup, name="sign_up"),
    # path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_changed.html'), name="pass_changed"),
    # path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name="ch_pass"),
    # path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="reset_pass"),
    # path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="reset_done"),
    path('accounts/', include('django.contrib.auth.urls')),

]
