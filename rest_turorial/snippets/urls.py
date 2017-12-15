from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
# from django.urls import path
from . import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),

    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)
