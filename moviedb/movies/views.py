# movies/views.py
from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.shortcuts import redirect
from .forms import MovieForm
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
def movie_detail_view(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/movie_detail.html', context)

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')  # Replace with your movie list URL name
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})
