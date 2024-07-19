from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Announcement, Like
from .serializers import AnnouncementSerializer


def documentation(request):
    return render(request, 'api/documentation.html')


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        announcement = get_object_or_404(Announcement, pk=pk)
        user_id = request.data.get('user_id')
        like, created = Like.objects.get_or_create(user=user_id, announcement=announcement)

        if not created and like.is_active:
            like.is_active = False
            like.save()
            return Response({'status': 'like removed'})
        elif not created:
            like.is_active = True
            like.save()
            return Response({'status': 'like added'})
        return Response({'status': 'like created'})
