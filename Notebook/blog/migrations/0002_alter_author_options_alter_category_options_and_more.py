# Generated by Django 4.1.7 on 2023-03-02 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['id'], 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['id'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['id'], 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='socialnetworkprofile',
            options={'ordering': ['id'], 'verbose_name': 'Social Network Profile', 'verbose_name_plural': 'Social Network Profiles'},
        ),
        migrations.AlterModelOptions(
            name='socialnetworktypes',
            options={'ordering': ['id'], 'verbose_name': 'SocialNetworkType', 'verbose_name_plural': 'Social Network Types'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id'], 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]
