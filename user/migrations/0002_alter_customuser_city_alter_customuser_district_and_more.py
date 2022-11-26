# Generated by Django 4.1.3 on 2022-11-20 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.city', to_field='uid'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.district', to_field='uid'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.ward', to_field='uid'),
        ),
    ]