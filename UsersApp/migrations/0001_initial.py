# Generated by Django 2.2.24 on 2022-03-02 16:41

from django.db import migrations, models
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('state', models.PositiveIntegerField(default=0)),
                ('creationDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
