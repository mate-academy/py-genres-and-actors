from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Actor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
            ],
        ),
    ]
