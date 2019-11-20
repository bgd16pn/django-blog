from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'', include('myapp.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^cadmin/', include('cadmin.urls')),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
