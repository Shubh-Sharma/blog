from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from comments.api.serializers import CommentListSerializer
from accounts.api.serializers import UserDetailSerializer
from comments.models import Comment
from posts.models import Post


post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)
post_delete_url = HyperlinkedIdentityField(
    view_name='posts-api:delete',
    lookup_field='slug'
)


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish'
        ]


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'content',
            'publish',
            'user'
        ]

    # def get_user(self, obj):
    #     return str(obj.user.username)


class PostDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'image',
            'title',
            'slug',
            'content',
            'publish',
            'user',
            'comments',
        ]

    def get_comments(self, obj):
        # content_type = obj.get_content_type()
        # object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentListSerializer(c_qs, many=True).data
        return comments

    # def get_user(self, obj):
    #     return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image