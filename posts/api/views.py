from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from posts.models import Post
from .serializers import *
from .pagination import *


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]    # ?search= and ?ordering=
    search_fields = ['title', 'content', 'user__first_name']
    pagination_class = PostPageNumberPagination # PostLimitOffsetPagination # PageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query)|
                    Q(user__last_name__icontains=query)
                ).distinct()
        return queryset_list



class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]