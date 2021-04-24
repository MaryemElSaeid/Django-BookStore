from django.contrib import admin
from django.urls import path,include
 
urlpatterns = [
    path("",include ('django.contrib.auth.urls')),
    path("",include("accounts.urls")),
    path('admin/', admin.site.urls),
    path('booklets/', include("booklets.urls")),
    path('api/booklets/',include("booklets.api.urls")),
]