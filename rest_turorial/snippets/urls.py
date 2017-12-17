from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
# from django.urls import path
from . import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlights/$',
        views.SnippetHighlight.as_view()),
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)
