# Generated by Django 4.0.4 on 2022-10-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_answer_content_alter_question_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(height_field=400, null=True, upload_to='image', width_field=400),
        ),
    ]
