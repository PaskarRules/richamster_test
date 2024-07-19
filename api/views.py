from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from .models import Announcement, Like
from .serializers import AnnouncementSerializer


def documentation(request):
    return render(request, 'api/documentation.html')


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get_permissions(self):
        """
        Returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def like(self, request, pk=None):
        """
        Allows any user to like or unlike an announcement.
        """
        announcement = get_object_or_404(Announcement, pk=pk)
        user_id = request.data.get('user_id', None)

        if not user_id:
            return Response({'error': 'User ID is required'}, status=400)

        like, created = Like.objects.get_or_create(user=user_id, announcement=announcement)

        if not created:
            like.is_active = not like.is_active
            like.save()
            status = 'like added' if like.is_active else 'like removed'
        else:
            status = 'like created'

        return Response({'status': status})
