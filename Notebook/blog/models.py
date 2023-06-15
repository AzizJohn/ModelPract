from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['id']


class Subscriber(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Profession(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="photos/author%Y/%m/%d/", verbose_name="avatar")
    bio = models.TextField()
    subscribers = models.ManyToManyField(Subscriber)
    professions = models.ManyToManyField(Profession)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['id']


class Post(models.Model):
    TYPE_CHOICES = (
        ('RECENTLY', 'Recently'),
        ('DRAFT', 'Draft'),
        ('POPULAR', 'Popular'),
        ('ACTUAL', 'Actual'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to="photos/post/%Y/%m/%d/", verbose_name="image")
    short_description = models.CharField(max_length=255)
    description = RichTextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    tags = models.ManyToManyField(Tag)
    time_to_read = models.PositiveIntegerField()
    views_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']


class Comment(models.Model):
    content = models.TextField()
    subscriber_id = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['id']


class SocialNetworkTypes(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="photos/social_media/%Y/%m/%d/", verbose_name="image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SocialNetworkType'
        verbose_name_plural = 'Social Network Types'
        ordering = ['id']


class SocialNetworkProfile(models.Model):
    social_network_type_id = models.ForeignKey(SocialNetworkTypes, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    profile_link = models.CharField(max_length=100)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Social Network Profile'
        verbose_name_plural = 'Social Network Profiles'
        ordering = ['id']


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['id']
