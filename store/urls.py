from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shopPage, name='product.index'),
    path('product/<slug:slug>/', views.singleProduct, name='product.show'),
    path('category/', views.category, name='category.index'),
    path('category/<slug:slug>', views.singleCategory, name='category.show'),
    path('brand/<slug:slug>', views.singleBrand, name='brand.show'),


    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)