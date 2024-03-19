from django.urls import path
from .import views
urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('employees_login/',views.employees_login,name='employees_login'),
    path('userlog/',views.userlog,name='userlog'),
    path('userlog_c/',views.userlog_c,name='userlog_c'),
    path('detailview/',views.detail_view,name='detail_view'),
    path('detailview_c/',views.detail_view_c,name='detail_view_c'),
    path('',views.home,name='home'),
    path('dashbord/',views.dashbord,name='dashbord'),
    path('register_c/',views.register_c,name='register_c'),
    path('customer_login/',views.userlog_c,name='customer_log'),
    path('customerprofile/',views.customerprofile,name='customerprofile'),
    path('customerlogout/',views.customerlogout,name='customerlogout'),
    path('staffprofile/',views.staffprofile,name='staffprofile'),
    path('stafflogout/',views.stafflogout,name='stafflogout'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('staff_update/',views.staff_update,name='update'),
    path('roompage/',views.roompage,name='roompage'),
    path('roomdisplay/',views.roomdisplay,name='roomdisplay'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    
   
]