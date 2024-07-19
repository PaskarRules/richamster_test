# from django.contrib import admin
# from .models import Announcement, Like
#
#
# class AnnouncementAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'date', 'like_count')
#     search_fields = ('title', 'description', 'user__username')
#     list_filter = ('date', 'user')
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         return queryset
#
#     def like_count(self, obj):
#         return obj.like_count
#
#     like_count.admin_order_field = 'like'
#     like_count.short_description = 'Active Likes'
#
#     def user_full_name(self, obj):
#         return f"{obj.user.first_name} {obj.user.last_name}"
#
#     user_full_name.admin_order_field = 'user__first_name'
#     user_full_name.short_description = 'User Name'
#
#
# admin.site.register(Announcement, AnnouncementAdmin)
# admin.site.register(Like)
from django.contrib import admin
from .models import Announcement, Like, Dislike


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'like_count', 'dislike_count')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('date', 'user')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    def like_count(self, obj):
        return obj.like_count

    like_count.admin_order_field = 'like'
    like_count.short_description = 'Active Likes'

    def dislike_count(self, obj):
        return obj.dislike_count

    dislike_count.admin_order_field = 'dislike'
    dislike_count.short_description = 'Active Dislikes'

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    user_full_name.admin_order_field = 'user__first_name'
    user_full_name.short_description = 'User Name'


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Like)
admin.site.register(Dislike)
