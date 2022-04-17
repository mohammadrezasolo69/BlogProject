from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # My URl
    path('account/', include('accounts.urls')),
    path('', include('blog.urls')),
]
