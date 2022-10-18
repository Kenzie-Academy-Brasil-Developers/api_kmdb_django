from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from project.pagination import CustomPageNumberPagination

from movies.models import Movie
from users.models import User

from .permissions import IsOwner, MyPermissions
from .models import Review
from .serializer import ReviewSerializer


class ReviewView(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyPermissions]

    def get(self, request: Request, movie_id: int) -> Response:
        reviews_data = Review.objects.filter(movie=movie_id)
        result_page = self.paginate_queryset(reviews_data, request, view=self)
        reviews = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(reviews.data)

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = Review.objects.filter(movie_id=movie.id, critic=request.user.id)

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if len(reviews) > 0:
            return Response(
                {"detail": "Review already exists"}, status.HTTP_403_FORBIDDEN
            )

        serializer.save(critic=request.user, movie=movie)

        return Response(serializer.data, status.HTTP_201_CREATED)


class ReviewDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]

    def get(self, request: Request, movie_id: int, review_id: int) -> Response:
        review_data = get_object_or_404(Review, id=review_id)
        review = ReviewSerializer(review_data)

        return Response(review.data)

    def delete(self, request: Request, movie_id: int, review_id: int) -> Response:
        review = get_object_or_404(Review, id=review_id)
        self.check_object_permissions(request, review)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
