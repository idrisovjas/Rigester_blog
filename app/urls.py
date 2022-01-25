from django.urls import  path
from .views import PostView,Tasnif,admin,Qosh


urlpatterns  = [
    path('',PostView.as_view() ,name='home'),
    path('tasnif/',Tasnif.as_view(),name='bosh'),
    path('admin/',admin.as_view,name='admin'),
    path('post/<int:pk>/',Qosh.as_view(),name='qosh'),

]
