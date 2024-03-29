#from django.conf import settings
#from django.conf.urls.static import static

from django.conf.urls import url
#from django.contrib import admin

from .views import (
    ProductListView,
    #product_list_view,
    #ProductDetailView,
    #product_detail_view,
    #ProductFeaturedListView,
    #ProductFeaturedDetailView,
    ProductDetailSlugView,
    )

#from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    #url(r'^$', home_page),
    #url(r'^about/$', about_page),
    #url(r'^contact/$', contact_page),
    #url(r'^login/$', login_page),
    #url(r'^register/$', register_page),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    #url(r'^featured/$', ProductFeaturedListView.as_view()),
    #url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    #url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    #url(r'^products-fbv/$', product_list_view),
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

    
 ]

#if settings.DEBUG:
	#urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)