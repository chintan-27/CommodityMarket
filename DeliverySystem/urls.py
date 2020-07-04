from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('courierdashboard/',views.CourierDashboard,name="CourierDashboard"),
    path('deliverydashboard/',views.DeliveryDashboard,name="DeliveryDashboard"),
    path('truckdashboard/',views.TruckDashboard,name="TruckDashboard"),
    path('delivered/<str:ordercode>/',views.Delivered,name="Delivered"),
    path('trukdelivered/<str:ordercode>/',views.TruckDelivered,name="TruckDelivered"),
    path('assigndelivery/<str:ordercode>/<str:city>/',views.assignDelivery,name="assignDelivery"),
    ]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
