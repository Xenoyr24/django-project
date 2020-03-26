"""devdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import logout

from accounts import views as accounts_views


#from products.views import (
#    ProductListView,
#    product_list_view,
#    ProductDetailView,
#    product_detail_view,
#    ProductFeaturedListView,
#    ProductFeaturedDetailView,
#    ProductDetailSlugView
#   )
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from accounts.views import login_page, register_page, logout_page, guest_register_view
from .views import home_page, test_page
from garden.views import  about_page, contact_page, testimonial_page, gallery_page, services_page, estimation_tool


from addresses.views import (checkout_address_create_view)

from orders.views import LibraryView

urlpatterns = [


    url(r'^$', home_page, name='home'),
    url(r'^admin/', include(admin.site.urls)),
##########################################################################################################

                                           #profile urls

    url(r'^profile/edit/$', accounts_views.edit_profile, name ='edit_profile'),
    url(r'^profile/$', accounts_views.profile, name='profile'),

##########################################################################################################

    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
#####################################################################################################    



    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^testimonial/$', testimonial_page, name='testimonial'),
    url(r'^services/$', services_page, name='services'),
    url(r'^gallery/$', gallery_page, name='gallery'),


    url(r'^login/$', login_page, name='login'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^register/$', register_page, name='register'),
    

###################################################################################################

    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^orders/', include("orders.urls", namespace='orders')),



###############################################################################################



    url(r'^tool/$', estimation_tool, name='tool'),


###################################################################################################

                                      #login forgot password url

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    
#########################################################################################################


    #url(r'^account_activation_sent/$', accounts_views.account_activation_sent, name='account_activation_sent'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',accounts_views.activate, name='activate'),



    url(r'^test/$', test_page, name='test'),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html'))

    #url(r'^cart/$', cart_home, name='cart'),
    #url(r'^featured/$', ProductFeaturedListView.as_view()),
    #url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    #url(r'^products/$', ProductListView.as_view()),
    #url(r'^products-fbv/$', product_list_view),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    #url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    #url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    ]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)