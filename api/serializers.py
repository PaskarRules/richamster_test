from rest_framework import serializers
from .models import Announcement, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'announcement', 'user', 'is_active', 'date']


class AnnouncementSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = ['id', 'user', 'title', 'description', 'date', 'likes', 'like_count']
