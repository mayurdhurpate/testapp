from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()



# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('hello.urls')),
]
