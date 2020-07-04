from django.urls import path
from . import views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings

urlpatterns = [
    path('', views.indexView, name="home"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('commodity/',views.CommoditiesAdd,name='AddCommodities'),
    path('retailshop/',views.AllCommoditiesRetail,name='retailshop'),
    path('retailshop/price/HL/',views.AllCommoditiesRetailPriceHL,name='retailshop'),
    path('retailshop/price/LH/',views.AllCommoditiesRetailPriceLH,name='retailshop'),
    path('retailshop/rating/',views.AllCommoditiesRetailRating,name='retailshop'),
    path('retailshop/type/abc/<str:type>/',views.AllCommoditiesRetailType,name='retailshop'),
    path('onecom/<str:comcode>/',views.OneCommodity,name='OneCommodity'),
    path('feedback/<str:comcode>/',views.Feedback,name='Feedback'),
    path('onecombulk/<str:comcode>/',views.OneCommodityBulk,name='OneCommodityBulk'),
    path('cart/',views.CartView,name='Cart'),
    path('buycart/',views.BuyCart,name='BuyCart'),
    path('wholesaleshop/',views.ManuFacturerShop,name='wholesaleshop'),
    path('confirm/<str:comcode>/<str:weight>/',views.Confirm,name='ConfirmOrder'),
    path('confirmbulk/<str:comcode>/<str:weight>/',views.ConfirmBulk,name='ConfirmBulkOrder'),
    path('addcart/<str:comcode>/<str:weight>/',views.AddToCart,name='AddToCart'),
    path('placeorder/<str:comcode>/<str:weight>/<str:type>/',views.OrderPlace,name='PlaceOrder'),
    path('placebulkorder/<str:comcode>/<str:weight>/<str:type>/',views.OrderPlaceBulk,name='PlaceBulkOrder'),
    ]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
