# Generated by Django 2.2.4 on 2019-08-29 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysqlapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='Marks',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.DeleteModel(
            name='Users1',
        ),
        migrations.DeleteModel(
            name='Users2',
        ),
        migrations.DeleteModel(
            name='Users3',
        ),
        migrations.DeleteModel(
            name='Users4',
        ),
    ]
