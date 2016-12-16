from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^index/', include('expense_uploader.urls')),
    url(r'^admin/', admin.site.urls),
]