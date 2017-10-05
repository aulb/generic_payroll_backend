from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^api/report/$', views.ReportList.as_view()),
    url(r'^api/time_report/', views.TimeReportList.as_view()),
    url(r'^api/job_group/$', views.JobGroupList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
