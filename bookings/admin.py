from django.contrib import admin
from .models import Movie, Seat, Booking

# admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Booking)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'image_url') 

admin.site.register(Movie, MovieAdmin)