from django.conf.urls import patterns, include, url

from django.contrib import admin

from models1 import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangomodel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),    
    url(r'^users/', 'models1.views.get_user'),
    url(r'^allusers/', 'models1.views.get_all_users'),
    url(r'^adduser/', 'models1.views.add_user'),
    url(r'^updatemail/', 'models1.views.update_user_email'),
    url(r'^deleteuser/', 'models1.views.delete_user'),

)
