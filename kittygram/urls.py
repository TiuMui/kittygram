from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   # path('cats/', cat_list),
   # path('cats/<int:pk>/', cats_detail),
   # path('cats/', APICat.as_view()),
   # path('cats/', CatList.as_view()),
   # path('cats/<int:pk>/', CatDetail.as_view()),
   path('', include(router.urls))
   # path('hello/', hello)
]
