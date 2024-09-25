from django.urls import path
from .views import index, t_login, l_room, t_myRoom


urlpatterns = [
    path('', index, name="index"),
    path('tenant/login', t_login, name="tenant_login"),
    path('owner/rooms', l_room, name="tenant_room_page"),
    path('owner/bills', t_myRoom, name="landlord_bills_page")
]