from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico'), name='favicon'),

urlpatterns = [
    # path('', login_user, name='login'),
    path('admin/', admin.site.urls),
    path('', include('engine.urls')),
]
