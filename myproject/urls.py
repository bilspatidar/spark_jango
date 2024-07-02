"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/categories/', include('modules.products.categories.urls')),
    path('api/subcategories/', include('modules.products.subcategories.urls')),
    path('api/userdocuments/', include('modules.products.user_documents.urls')),
    path('api/form_fields/', include('modules.products.form_field.urls')),
    path('api/document/', include('modules.products.document.urls')),
    path('api/document_type/', include('modules.products.document_type.urls')),
    path('api/service/', include('modules.products.service.urls')),
    path('api/tagging/', include('modules.products.tagging.urls')),
    path('api/review_rating/', include('modules.products.review_rating.urls')),
    path('api/contact/', include('modules.products.contact.urls')),
    path('api/currency/', include ('modules.products.currency.urls')),
]
