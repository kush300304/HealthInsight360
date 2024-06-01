from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='minor-home'),
    path('logout/',auth_views.LogoutView.as_view(template_name='minorproject/logout.html'),name='logout'),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('dashboard/<str:user>/', views.dashboard, name='dashboard'),
    path('login/',views.logins,name='login-home'),
    path('search/',views.search,name='search-home'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('searchmed/', views.search_medicines, name='search-medicines'),
    path('insight/', views.insights, name='insightt'),
    path('sent_email/', views.send_email, name='emaill'),
    path('reports/<str:user>/', views.reports, name='reports'),
    path('records/<str:encount_id>/', views.records, name='records'),
    path('encounter/',views.encounters,name='encounter'),
]