from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):
    movies = Movie.objects.all()  # Fetch up to 5 movies
    return render(request, 'bookings/home.html', {'movies': movies})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

@login_required(login_url='/accounts/login/')  # Restricts access
def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    if request.method == "POST":
        seat_id = request.POST.get("seat")
        if not seat_id:
            return render(request, 'bookings/seat_booking.html', {
                'movie': movie,
                'seats': seats,
                'error': "Please select a seat before booking."
            })

        try:
            seat = Seat.objects.get(id=seat_id, movie=movie, is_booked=False)
            seat.is_booked = True
            seat.save()
            return render(request, 'bookings/seat_booking.html', {
                'movie': movie,
                'seats': seats,
                'success': f"Seat {seat.seat_number} booked successfully!"
            })
        except Seat.DoesNotExist:
            return render(request, 'bookings/seat_booking.html', {
                'movie': movie,
                'seats': seats,
                'error': "Selected seat is not available. Please choose another."
            })

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'bookings/movie_detail.html', {'movie': movie})