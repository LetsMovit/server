from django.contrib import admin
from .models import Genre, Movie, Location, LocationComment
# Register your models here.


admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Location)
admin.site.register(LocationComment)