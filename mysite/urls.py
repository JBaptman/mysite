from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls import include, url

urlpatterns = [
    url(r'^(/)?$', RedirectView.as_view(url='/microblog/')), #Set the default page to the app microblog, would have put the login page, but as you can see I didn't really manage to realize this feature.
    url(r'^admin/', admin.site.urls),
    url(r'^microblog/', include('microblog.urls')),
]