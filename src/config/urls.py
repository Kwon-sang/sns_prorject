from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(TemplateView.as_view(template_name='index.html')), name='root'),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # Debug-toolbar setting
    import debug_toolbar
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
