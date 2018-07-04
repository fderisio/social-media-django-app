"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include
from project.motion_app.views import OverviewView, PostDetailsView, NewPostView, NewPostTemplateView, SignUpView
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from project.api.auth.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registration URLs
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),

    # Rest framework
    url(r'^api-auth/', include('rest_framework.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include('project.api.auth.urls', namespace='api')),

    # Template URLs
    path('', OverviewView.as_view(), name='overview'),
    path('<int:post_id>/', PostDetailsView.as_view(), name='post_details'),
    path('new-post/', NewPostView.as_view(), name='new_post_view'),
    path('new-post-template-view/', NewPostTemplateView.as_view(), name='new_post_template_view'),

]
