from rest_framework import serializers
from .models import Announcement, Like, Dislike


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'announcement', 'user', 'is_active', 'date']


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ['id', 'announcement', 'user', 'is_active', 'date']


class AnnouncementSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    dislikes = DislikeSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    dislike_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Announcement
        fields = ['id', 'user', 'title', 'description', 'date', 'likes', 'like_count', 'dislikes', 'dislike_count']
