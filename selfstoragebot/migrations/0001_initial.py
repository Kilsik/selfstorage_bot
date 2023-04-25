# Generated by Django 3.2.18 on 2023-04-25 14:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('telegram_id', models.IntegerField(unique=True)),
                ('username', models.CharField(max_length=64, null=True, verbose_name='User Name')),
                ('first_name', models.CharField(max_length=256, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Last Name')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('is_admin', models.BooleanField(blank=True, default=False, null=True, verbose_name='Администратор')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='InvitationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_id', models.CharField(max_length=255, unique=True)),
                ('click_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouses',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True, unique=True, verbose_name='Name')),
                ('address', models.CharField(max_length=1024, null=True, unique=True, verbose_name='Warehouse Address')),
            ],
            options={
                'verbose_name': 'Warehouse',
                'verbose_name_plural': 'Warehouses',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(default='1', max_length=100, unique=True, verbose_name='Order number')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Order Date')),
                ('weight', models.IntegerField(default=0, null=True, verbose_name='Weight of item')),
                ('volume', models.IntegerField(default=0, null=True, verbose_name='Volume of item')),
                ('store_duration', models.IntegerField(null=True, verbose_name='Duration of storage')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name of item')),
                ('cost', models.FloatField(default=0, verbose_name='Storage cost')),
                ('address_from', models.CharField(blank=True, max_length=250, null=True, verbose_name='Address of picking up')),
                ('address_to', models.CharField(blank=True, max_length=250, null=True, verbose_name='Address of returning')),
                ('date_delivery_from', models.DateTimeField(blank=True, null=True, verbose_name='Date of delivery to the warehouse')),
                ('delivery_status', models.CharField(choices=[('0', 'Создан'), ('1', 'В работе'), ('2', 'Ожидает доставки'), ('3', 'Курьер в пути'), ('4', 'Груз на складе'), ('5', 'Возвращен'), ('6', 'Истех срок хранения')], db_index=True, default=0, max_length=15, null=True, verbose_name='Статус доставки заказа')),
                ('type_delivery', models.CharField(choices=[('0', 'Самостоятельно'), ('1', 'Курьером')], db_index=True, max_length=15, null=True, verbose_name='Тип доставки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='selfstoragebot.clients', verbose_name='Client')),
                ('warehouse', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='selfstoragebot.warehouses', verbose_name='Warehouse')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
