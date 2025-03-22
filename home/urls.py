from django.urls import path



from .views import *
urlpatterns=[
    path('', home_view, name='home'),
    path('blog/', blog_view, name='blog'),

    path('blogg/', blogg_view, name='about'),


    # path('contact', index_view, name='contact'),
    # path('gallery', gallery_view(), name='home'),
    # path('project_detail', index_view, name='home'),
    # path('projects', index_view, name='home'),
    # path('', index_view, name='home'),
    # path('', index_view, name='home'),

]