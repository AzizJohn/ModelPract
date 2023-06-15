from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Tag, Subscriber, Profession, Author, Post, Comment, SocialNetworkProfile, \
    SocialNetworkTypes, Contact


# for Person model
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


class SubscriberTranslationOptions(TranslationOptions):
    fields = ('full_name',)


class ProfessionTranslationOptions(TranslationOptions):
    fields = ('title',)


class AuthorTranslationOptions(TranslationOptions):
    fields = ('full_name', 'bio',)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)


class CommentTranslationOptions(TranslationOptions):
    fields = ('content',)


class SocialNetworkTypesTranslationOptions(TranslationOptions):
    fields = ('name',)


class SocialNetworkProfileTranslationOptions(TranslationOptions):
    fields = ('nickname',)


class ContactTranslationOptions(TranslationOptions):
    fields = ('name', 'subject', 'message',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Subscriber, SubscriberTranslationOptions)
translator.register(Profession, ProfessionTranslationOptions)
translator.register(Author, AuthorTranslationOptions)
translator.register(Post, PostTranslationOptions)
translator.register(Comment, CommentTranslationOptions)
translator.register(SocialNetworkTypes, SocialNetworkTypesTranslationOptions)
translator.register(SocialNetworkProfile, SocialNetworkProfileTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
