from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns


from .views import *
urlpatterns=[
    path('', home_view, name='home'),
    path('blog/', blog_view, name='blog'),
    path('blogg/', blogg_view, name='about'),
    path('send_email/', send_email, name='send_email'),
    path("contact_view/", contact_view, name="contact_view"),
    path('i18n/', include('django.conf.urls.i18n')),
    path('set-language/', switch_language, name='set_language'),
]





