from django.urls import path, include
from rest_framework import routers

from blog.views import ArticleViewSet, ReporterViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'reporters', ReporterViewSet)
router.register(r'contact', ContactViewSet)

'''  ---------------------------------------  '''
app_name = 'blog'
urlpatterns = [
  path('', include(router.urls)),
]
