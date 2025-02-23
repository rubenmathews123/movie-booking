from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from .views import home, movie_list, seat_booking, booking_history, movie_detail
from django.contrib.auth import views as auth_views


# Create API Router
router = DefaultRouter()
# router.register(r'movies', MovieViewSet)  
# router.register(r'seats', SeatViewSet)
# router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # Frontend Pages (HTML Templates)
    path('', home, name='home'),
    path('movies/', movie_list, name='movie_list'), 
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'), 
    path('movies/<int:movie_id>/book/', seat_booking, name='seat_booking'),
    path('bookings/history/', booking_history, name='booking_history'),

    path('accounts/', include('django.contrib.auth.urls'))

]
