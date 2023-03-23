import json

from django.http import JsonResponse
from django.contrib.auth.models import User
from .service import resultado


def recebe_resultado(request):
    respostas = request.POST['resultado']
    user = request.user.id
    resultado.contabilizaResultado(respostas, user)

    return JsonResponse({})

def get_resultado(request):
    user = request.user.id
    resultado_filmes = resultado.pega_resultado(user)
    return JsonResponse(resultado_filmes)

def save_note(request: HttpRequest) -> HttpResponse:
    movies = Movie.objects.all()
    for movie in movies:
        rating = Rating.objects.filter(movie=movie, user=request.user).first()
        movie.user_rating = rating.rating if rating else 0
    return render(request, "index.html", {"movies": movies})

def rate(request: HttpRequest, movie_id: int, rating: int) -> HttpResponse:
    movie = Movie.objects.get(id=movie_id)
    Rating.objects.filter(movie=movie, user=request.user).delete()
    movie.rating_set.create(user=request.user, rating=rating)
    return index(request)