"""djangoPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework import routers
from lob import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'board', views.BoardViewset)
router.register(r'food',views.FoodViewset)
router.register(r'basket',views.BasketViewset)
router.register(r'user',views.UserViewset)
router.register(r'calendar',views.CalendarViewset)
router.register(r'comment',views.CommentViewset)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
