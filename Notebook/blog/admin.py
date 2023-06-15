from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    #fields = ('name',)
    # readonly_fields = ('time_create', 'time_update', 'get_html_photo')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')  # fields which we can display on panel
    list_display_links = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    #fields = ('name',)  # fields which we can redaction


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'date_joined')
    list_display_links = ('full_name', 'email')
    search_fields = ('full_name',)
    list_filter = ('full_name', 'date_joined')
    fields = ('full_name', 'email')


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'get_html_photo', 'bio')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name',)

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50>")

    get_html_photo.short_description = "avatar"


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'type', 'time_to_read', 'views_count', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'type', 'tags', 'views_count',)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('type', 'tags', 'time_to_read', 'views_count', 'created_at',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = "avatar"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'subscriber_id', 'post_id')
    list_display_links = ('id', 'created_at', 'subscriber_id', 'post_id')
    list_filter = ('created_at', 'subscriber_id', 'post_id',)


class SocialNetworkTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def get_html_photo(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_photo.short_description = "icon"

class SocialNetworkProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'profile_link', 'author_id', 'social_network_type_id')
    list_display_links = ('id', 'nickname', 'profile_link', 'author_id')
    search_fields = ('nickname', 'author_id', 'social_network_type_id',)
    list_filter = ('social_network_type_id',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'date_sent')
    list_display_links = ('id', 'name', 'email', 'date_sent')
    list_filter = ('date_sent',)
    search_fields = ('name', 'email',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(SocialNetworkTypes, SocialNetworkTypesAdmin)
admin.site.register(SocialNetworkProfile, SocialNetworkProfileAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.site_title = 'NoteBook'
admin.site.site_header = 'NoteBook'

"""class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        'title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"
"""
