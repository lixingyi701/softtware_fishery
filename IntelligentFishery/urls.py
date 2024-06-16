"""
URL configuration for IntelligentFishery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from fishery.views import (
    login,
    register,
    homepage,
    user,
    illustration,
    main_info,
    underwater_system,
    data_center,
    intelligence_center,
    admin_management
)

urlpatterns = [
    path("fishery/login/", login, name='login'),
    path("fishery/register/", register, name='register'),
    path("fishery/homepage/", homepage, name='homepage'),
    path("fishery/user/", user, name='user'),
    path("fishery/illustration/", illustration, name='illustration'),
    path("fishery/main-info/", main_info, name='main_info'),
    path("fishery/underwater-system/", underwater_system, name='underwater_system'),
    path("fishery/data-center/", data_center, name='data_center'),
    path("fishery/intelligence-center/", intelligence_center, name='intelligence_center'),
    path("fishery/admin-management/", admin_management, name='admin_management'),
]