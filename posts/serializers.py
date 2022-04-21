from rest_framework import serializers

from posts.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    class Meta:
        model: Post = Post
        fields: list = ['id', 'created', 'poster', 'poster_id', 'title', 'url']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model: Vote = Vote
        fields = ['id']

