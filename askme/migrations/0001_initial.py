# Generated by Django 4.2 on 2023-04-10 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('avatar', models.ImageField(default='static/img/ava.png', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('usage_amount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UsersLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField(choices=[(-1, 'DIS'), (1, 'LIKE')])),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='askme.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=10000)),
                ('ask_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('answers_amount', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('solved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='askme.profile')),
                ('tags', models.ManyToManyField(blank=True, to='askme.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000)),
                ('answ_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_verified', models.BooleanField(default=False)),
                ('rating', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='askme.profile')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='askme.question')),
            ],
        ),
    ]