from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.urls import include
from .admin import admin_site
from conf import settings
from . import views
from receivables.wiews import WorkTimeJournalView

#----- Refactor all above as under -----
from prjdash import urls as prjdash_urls


urlpatterns = i18n_patterns(
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^select2/', include('django_select2.urls')),
    url(r'^admin/', admin_site.urls, name='admin'),
    url(r'^receivables/tjournal/(?P<project_id>[0-9]+)/(?P<date>\d{4}-\d{2}-\d{2})$', WorkTimeJournalView.as_view(), name='tjournal'),
    url(r'^receivables/tjournal/(?P<project_id>[0-9]+)/(?P<date>\d{4}-\d{2}-\d{2})/(?P<modify_id>[0-9]+)$', WorkTimeJournalView.as_view(), name='tjournal'),
    url(r'^v1/pdash/', include(prjdash_urls.urlpatterns)),
    prefix_default_language=False
)

if settings.DEBUG:
    #from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    #from django.conf.urls.static import static
    
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

    #urlpatterns += staticfiles_urlpatterns()
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)