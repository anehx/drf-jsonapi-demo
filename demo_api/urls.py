from demo_api               import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'posts',    views.PostViewSet,    'post')
router.register(r'comments', views.CommentViewSet, 'comment')

urlpatterns = router.urls
