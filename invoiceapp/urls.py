from django.urls import path
from invoiceapp import views


urlpatterns=[
    path('admininfo/',views.AdminInfoViewset),
    path('users/',views.UserViewset),
    path('links/',views.LinkViewset),
    path('singleuser/',views.SingeUserViewset),
    path('singleuser/link',views.SingleUserLinkViewset),
    path('singleadmin/',views.SingleAdminInfoViewset)
]