from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from rest_framework.authentication import TokenAuthentication
from .permissions import MyPermissions

from movies.models import Movie
from movies.serializers import MovieSerializer
from project.pagination import CustomPageNumberPagination


class MoviesView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyPermissions]

    def get(self, request: Request) -> Response:
        movies_data = Movie.objects.all()
        result_page = self.paginate_queryset(movies_data, request, view=self)
        movie = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(movie.data)

    def post(self, request: Request) -> Response:
        movie = MovieSerializer(data=request.data)
        movie.is_valid(raise_exception=True)
        movie.save()

        return Response(movie.data, status.HTTP_201_CREATED)


class MoviesDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyPermissions]

    def get(self, request: Request, movie_id: int) -> Response:
        movie_obj = get_object_or_404(Movie, id=movie_id)
        movie = MovieSerializer(movie_obj)

        return Response(movie.data)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, movie_id: int) -> Response:
        movie_obj = get_object_or_404(Movie, id=movie_id)
        movie = MovieSerializer(movie_obj, request.data, partial=True)
        movie.is_valid(raise_exception=True)
        movie.save()

        return Response(movie.data)