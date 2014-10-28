from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import BoatList, BoatDetail

# router = routers.DefaultRouter()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'peekapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/boats/$', BoatList.as_view(), name='boat_list'),
    url(r'^api/events/(?P<pk>[0-9]+)/$', BoatDetail.as_view(), name='boat_detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)
