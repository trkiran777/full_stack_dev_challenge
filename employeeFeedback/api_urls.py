from django.conf.urls import patterns,url
from employeeFeedback.api_views import EmployeeDetails

urlpatterns = patterns("employeeFeedback.api_views",
                       url(r'admin/employee-details/$', EmployeeDetails.as_view())
                       )