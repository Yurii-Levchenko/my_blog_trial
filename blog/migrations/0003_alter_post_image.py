# Generated by Django 5.0 on 2024-01-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_remove_post_tag_post_tags_alter_post_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="posts"),
        ),
    ]
