from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'employeeFeedback.views.landing_page', name='landing-page'),
                       url(r'^admin-home-page/$', 'employeeFeedback.views.admin_home_page', name='admin-home-page'),
                       url(r'^admin/performance-reviews/$', 'employeeFeedback.views.performance_reviews_page',
                           name='performance-reviews'),
                       url(r'^api/', include('employeeFeedback.api_urls')),
                       )