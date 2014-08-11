from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

from gallery.views import AlbumDetailView, AlbumListView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.views.home', name='home'),
    url(r'^works', AlbumListView.as_view(), name='album-list'),
    url(r'^contact/','pages.views.contact', name ='contact'),
    url(r'^album/(?P<pk>\d+)/$', AlbumDetailView.as_view(), name='album_detail'),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
