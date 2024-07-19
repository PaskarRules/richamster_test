from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_set.filter(is_active=True).count()

    @property
    def dislike_count(self):
        return self.dislike_set.filter(is_active=True).count()


class BaseReaction(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    user = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.announcement.title} - {'Active' if self.is_active else 'Inactive'} by User {self.user}"


class Like(BaseReaction):
    pass


class Dislike(BaseReaction):
    pass
