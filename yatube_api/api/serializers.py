from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, User, Group, Follow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        ref_name = 'ReadOnlyUsers'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    def validate_following(self, value):
        if value == self.context["request"].user:
            raise serializers.ValidationError()
        return value

    class Meta:
        fields = '__all__'
        model = Follow
