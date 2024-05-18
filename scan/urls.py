from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.getEmployees, name='emp'),
    path('employees/<pk>', views.getEmployeeDetail, name='emp-detail'),
    path('company-outlet',  views.CompanyOutletListCreate.as_view(), name='company-outlet'),
    path('company-outlet/<pk>', views.CompanyOutletDetail.as_view(), name='company-outlet-detail'),
    path('activity-log', views.ActivityEmpList.as_view(), name='activity-log'),
    path('activity-log/<int:id>/employees', views.ActivityEmpOutlet, name='activity-log-company'),
    path('activity-log/date-detail', views.ActivityDateDetailOutlet, name='activity-log-date-detail'),

    # path('activity-log/<pk>/company-outlet', views.ActivityEmpDetail.as_view(), name='activity-log-detail'),
    path('activity-log/<pk>', views.ActivityEmpDetail.as_view(), name='activity-log-detail'),


    path('employees/auth/login', views.empLogin, name='activity-login'),
    path('employees/auth/register', views.empRegister, name='activity-register'),
    path('employees/auth/logout', views.empLogout, name='activity-logout'),


]


# ]