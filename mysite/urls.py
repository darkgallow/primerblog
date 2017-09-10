from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'', include('blog.urls'))
=======
    url(r'', include('blog.urls')),
>>>>>>> 6052b96a2032128a731f1875014bccda0a6d34b3
]
