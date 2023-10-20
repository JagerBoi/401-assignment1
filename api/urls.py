from django.urls import path, re_path
from .views import part_detail, part_lists

urlpatterns = [
    path('parts/', part_lists),
    path('parts/<int:ID>/', part_detail),
]