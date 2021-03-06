# Generated by Django 2.1.1 on 2019-01-23 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='allow_multiple_choices',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question'),
        ),
    ]
